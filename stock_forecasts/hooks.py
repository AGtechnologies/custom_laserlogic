# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "stock_forecasts"
app_title = "Stock Forecasts"
app_publisher = "AGT Technologies"
app_description = "Stock Forecasts"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "agt.com"
app_license = "MIT"

#fixtures = ["Custom Field"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/stock_forecasts/css/stock_forecasts.css"
# app_include_js = "/assets/stock_forecasts/js/stock_forecasts.js"

# include js, css files in header of web template
# web_include_css = "/assets/stock_forecasts/css/stock_forecasts.css"
# web_include_js = "/assets/stock_forecasts/js/stock_forecasts.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "stock_forecasts.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "stock_forecasts.install.before_install"
# after_install = "stock_forecasts.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "stock_forecasts.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"stock_forecasts.tasks.all"
# 	],
# 	"daily": [
# 		"stock_forecasts.tasks.daily"
# 	],
# 	"hourly": [
# 		"stock_forecasts.tasks.hourly"
# 	],
# 	"weekly": [
# 		"stock_forecasts.tasks.weekly"
# 	]
# 	"monthly": [
# 		"stock_forecasts.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "stock_forecasts.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "stock_forecasts.event.get_events"
# }

