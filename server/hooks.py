from __future__ import unicode_literals
from frappe import __version__ as version


app_name = "server"
app_title = "server"
app_publisher = "akshay sharma"
app_description = "server description"
app_email = "akshaysharmaxyz12@gmail.com"
app_license = "mit"

# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/server/css/server.css"
# app_include_js = "/assets/server/js/server.js"

# include js, css files in header of web template
# web_include_css = "/assets/server/css/server.css"
# web_include_js = "/assets/server/js/server.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "server/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "server/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "server.utils.jinja_methods",
# 	"filters": "server.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "server.install.before_install"
# after_install = "server.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "server.uninstall.before_uninstall"
# after_uninstall = "server.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "server.utils.before_app_install"
# after_app_install = "server.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "server.utils.before_app_uninstall"
# after_app_uninstall = "server.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "server.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

doc_events = {
    "Student Detail": {
        "after_insert": "server.my_project.doctype.student_detail.student_detail.create_student_detail",
        "on_update": "server.my_project.doctype.student_detail.student_detail.update_student_detail",
        "on_trash": "server.my_project.doctype.student_detail.student_detail.delete_student_detail",

    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"server.tasks.all"
# 	],
# 	"daily": [
# 		"server.tasks.daily"
# 	],
# 	"hourly": [
# 		"server.tasks.hourly"
# 	],
# 	"weekly": [
# 		"server.tasks.weekly"
# 	],
# 	"monthly": [
# 		"server.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "server.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "server.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "server.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["server.utils.before_request"]
# after_request = ["server.utils.after_request"]

# Job Events
# ----------
# before_job = ["server.utils.before_job"]
# after_job = ["server.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"server.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# hooks.py

# def get_api_methods():
#     return {
#         "get_users": "server.my_project.doctype.create_user.create_user.get_users",
#         "create_user_from_student": "server.my_project.doctype.create_user.create_user.create_user_from_student"
#     }
