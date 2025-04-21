# your_app/overrides.py

import frappe

def website_context(context):
    # Add a custom variable
    context.my_key = "Hello from Frappe!"

    # Fetch user info if logged in
    if frappe.session.user != "Guest":
        context.user_email = frappe.session.user
        context.user_fullname = frappe.utils.get_fullname(frappe.session.user)
    
    # Custom website settings
    context.custom_settings = {
        "theme": "dark-mode",
        "show_banner": True
    }

def clear_website_cache(path=None):
    if path:
        # Clear cache for a specific page
        frappe.cache().delete_value(f"website_page:{path}")
        print(f"Cache cleared for: {path}")
    else:
        # Clear all website cache
        frappe.cache().delete_value("website_routes")
        frappe.cache().delete_value("website_cache")
        print("All website cache cleared!")

# def get_home_page(user=None):
#     if not user:
#         frappe.logger().info("Guest user detected, redirecting to index.")
#         return "index"  # Default homepage for guests

#     roles = frappe.get_roles(user)
#     frappe.logger().info(f"User: {user} | Roles: {roles}")

#     if "Customer" in roles:
#         frappe.logger().info("Redirecting user to orders page.")
#         return "orders"
#     if "Supplier" in roles:
#         frappe.logger().info("Redirecting user to bills page.")
#         return "bills"

#     frappe.logger().info("No matching role, redirecting to index.")
#     return "index"
