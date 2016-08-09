# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate, today

def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns(filters)
	data = get_data(filters)

	return columns,data

def get_columns(filters):
	"""return columns based on filters"""

	columns = [_("ITEM NO.") + ":Link/Item:140", _("ALT ITEM NO") + "::100", _("ITEM DESCRIPTION") + "::200",
		_("MIN") + ":Float:110", _("MAX") + ":Float:100",
		_("PO") + ":Float:100", _("SO") + ":Float:100",
		_("ON HAND") + ":Float:100", _("Reorder Qty") + ":Float:100"]

	return columns

def get_data(filters):
	bin_list = get_bin_list(filters)
	item_map = get_item_map(filters.get("item_code"))
	warehouse_company = {}
	data = []

	for bin in bin_list:
		item = item_map.get(bin.item_code)

		if not item:
			# likely an item that has reached its end of life
			continue

		# item = item_map.setdefault(bin.item_code, get_item(bin.item_code))
		company = warehouse_company.setdefault(bin.warehouse, frappe.db.get_value("Warehouse", bin.warehouse, "company"))

		re_order_qty = item.item_max -  bin.ordered_qty - bin.actual_qty + bin.reserved_qty

		data.append([item.item_code, item.item_name, item.description, item.item_min, item.item_max, bin.ordered_qty, bin.reserved_qty, bin.actual_qty, re_order_qty])

	return data

def get_bin_list(filters):
	conditions = []
	bin_list = frappe.db.sql("""select item_code, warehouse, sum(actual_qty) as actual_qty , planned_qty, indented_qty,
		sum(ordered_qty) as ordered_qty, sum(reserved_qty) as reserved_qty, reserved_qty_for_production, projected_qty
		from tabBin bin {conditions} group by item_code order by item_code""".format(conditions=" where " + " and ".join(conditions) if conditions else ""), as_dict=1)

	return bin_list

def get_item_map(item_code):
	"""Optimization: get only the item doc and re_order_levels table"""

	condition = ""
	if item_code:
		condition = 'and item_code = "{0}"'.format(frappe.db.escape(item_code, percent=False))

	items = frappe.db.sql("""select * from `tabItem` item
		where is_stock_item = 1
		and disabled=0
		{condition}
		and (end_of_life > %(today)s or end_of_life is null or end_of_life='0000-00-00')
		and exists (select name from `tabBin` bin where bin.item_code=item.name)"""\
		.format(condition=condition), {"today": today()}, as_dict=True)

	condition = ""
	if item_code:
		condition = 'where parent="{0}"'.format(frappe.db.escape(item_code, percent=False))

	reorder_levels = frappe._dict()
	for ir in frappe.db.sql("""select * from `tabItem Reorder` {condition}""".format(condition=condition), as_dict=1):
		if ir.parent not in reorder_levels:
			reorder_levels[ir.parent] = []

		reorder_levels[ir.parent].append(ir)

	item_map = frappe._dict()
	for item in items:
		item["reorder_levels"] = reorder_levels.get(item.name) or []
		item_map[item.name] = item

	return item_map