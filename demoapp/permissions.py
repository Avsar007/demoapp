# import frappe

# def todo_query(user):
#     if not user:
#         user = frappe.session.user  # Get current user if not provided

#     # SQL WHERE condition: User can see ToDo items they own or assigned
#     return "(`tabToDo`.owner = {user} OR `tabToDo`.assigned_by = {user})".format(
#         user=frappe.db.escape(user)  # Escape user to prevent SQL injection
#     )
import frappe

def todo_query(user):
    if not user:
        user = frappe.session.user  # Get login user

    # Check if the user is Administrator
    if user == "Administrator":
        return "" 

    # Restriction for normal users
    return "(`tabToDo`.owner = {user})".format(user=frappe.db.escape(user))
