import frappe

def clear_cache():
    # Clear specific cached values
    frappe.cache().hdel("demoapp_custom_cache")
    frappe.cache().hdel("another_cache_key")
    print("Custom cache cleared for DemoApp!")
