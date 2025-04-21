import frappe

def get_fullname(user):
    first_name, last_name = frappe.db.get_value("User", user, ["first_name", "last_name"])
    return f"{first_name} {last_name}"

def format_currency(value, currency="INR"):
    return f"{currency} {value}"

def to_uppercase(text):
    return text.upper() if text else ""