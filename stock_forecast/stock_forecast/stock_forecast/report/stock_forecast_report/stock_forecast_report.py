# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns(filters)

	return columns

def get_columns(filters):
	"""return columns based on filters"""

	columns = ["Item No:Link/Item:100", "Alt Item No::150", \
	"Item Description::140", "MIN::100", "MAX::100", "PO::100", "SO::100", "ON HAND::100"]

	return columns
