app_name = "demoapp"
app_title = "Demoapp"
app_publisher = "AK"
app_description = "It is a demo app"
app_email = "avsarkalola21@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "demoapp",
# 		"logo": "/assets/demoapp/logo.png",
# 		"title": "Demoapp",
# 		"route": "/demoapp",
# 		"has_permission": "demoapp.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/demoapp/css/demoapp.css"
# app_include_js = "/assets/demoapp/js/demoapp.js"

# include js, css files in header of web template
# web_include_css = "/assets/demoapp/css/demoapp.css"
# web_include_js = "/assets/demoapp/js/demoapp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "demoapp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# website_context hook

website_context = {
    "favicon": "/assets/demoapp/images/sigzen-favicon.svg",
    "brand_html": "<b>My Custom Portal</b>"
}

update_website_context = "demoapp.overrides.website_context"

# website Controller Context

# extend_website_page_controller_context = {
#     "frappe.www.404": "demoapp.pages.context_404"
# }

# web pages with dynamic routes

# get_web_pages_with_dynamic_routes = "demoapp.script.get_web_pages_with_dynamic_routes"

# website clear cache

website_clear_cache = "demoapp.overrides.clear_website_cache"

# website redirect 

website_redirects = [
    {"source": "/old-blog", "target": "/new-blog"},
    {"source": "/products(/.*)?", "target": "/store\1"},
    {"source": r'/search\?q=(.*)', "target": '/new-search?q=\1', "match_with_query_string": True}
]

# website route rules

website_route_rules = [
    {"from_route": "/projects/", "to_route": "demoapp/projects/project"}
]

# website path resolver

# website_path_resolver = "demoapp.custom_router.custom_resolver"

# website 404

# website_catch_all = "not_found"

# Default Homepage
homepage = "homepage"


# Calender
calendars = ["Library Membership"]


# portal Sidebar

standard_portal_menu_items = [
    {"title": "Greetings", "route": "/greetings", "role": "Website Manager"},
    {"title": "Orders", "route": "/orders", "role": "Website Manager"},
]

# brand html

brand_html = '<div><img src="/assets/demoapp/images/sigzen_favicon.svg" width="30"/> DemoApp</div>'
# base_template = "demoapp/templates/custom_base.html"

# Integration
# Braintree Success Page

braintree_success_page = "app.integrations.braintree_success_page"

# clear-cache

# clear_cache = "demoapp.cache.clear_cache"

# Document Hooks
# Modify List Query 

permission_query_conditions = {
    "ToDo": "demoapp.permissions.todo_query",
}

# include js in page    
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# doctype_list_js = {"Student": "public/js/student_list.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "demoapp/public/icons.svg"

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
jinja = {
    "methods": [
        "demoapp.jinja.methods",
        "demoapp.utils.get_fullname"
    ],
    "filters": [
        "demoapp.jinja.filters",
        "demoapp.utils.format_currency"
    ]
}

# Installation
# ------------

# before_install = "demoapp.install.before_install"
after_install = "demoapp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "demoapp.install.before_uninstall"
# after_uninstall = "demoapp.install.after_uninstall"

# Migration
# -----------

before_migrate = "demoapp.migrate.before_migrate"
after_migrate = "demoapp.migrate.after_migrate"

# File Hooks

# before_write_file = "demoapp.file.before_write"
# write_file = "demoapp.file.write_file"
# delete_file_data_content = "demoapp.file.delete_file"

# Email Hooks

# override_email_send = "demoapp.overrides.email.send"
# get_sender_details = "demoapp.overrides.email.get_sender_details"

# Extend BootInfo Hooks

# extend_bootinfo = "your_app.boot.boot_session"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "demoapp.utils.before_app_install"
# after_app_install = "demoapp.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "demoapp.utils.before_app_uninstall"
# after_app_uninstall = "demoapp.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "demoapp.notifications.get_notification_config"

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
# 	# "ToDo": "custom_app.overrides.CustomToDo",
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

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"demoapp.tasks.all"
# 	],
# 	"daily": [
# 		"demoapp.tasks.daily"
# 	],
# 	"hourly": [
# 		"demoapp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"demoapp.tasks.weekly"
# 	],
# 	"monthly": [
# 		"demoapp.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "demoapp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "demoapp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "demoapp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
auto_cancel_exempted_doctypes = ["Property"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["demoapp.utils.before_request"]
# after_request = ["demoapp.utils.after_request"]

# Job Events
# ----------
# before_job = ["demoapp.utils.before_job"]
# after_job = ["demoapp.utils.after_job"]

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
# 	"demoapp.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


# scheduler_events = {
#     "cron": {         
#         # "* * * * *": [
#         #     "demoapp.api.long_task"
#         # ],
#         "9 * * * *": [
#             # "demoapp.api.notify_me"
#             "demoapp.api.long_task"
#         ]
#     }
# }

# fixtures = [
#     "Custom Field"
# ]