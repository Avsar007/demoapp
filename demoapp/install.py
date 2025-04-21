# import frappe
# # logger = frappe.log_error("Install error occurred", "Install Error")
# # print(f"install.py is loaded! {logger}")

# def before_install():
#     print("before_install() is running!")

def after_install():
    print("after_install() is running!")

# # def before_uninstall():
# #     print("before_uninstall() is running!")

# # def after_uninstall():
# #     print("after_uninstall() is running!")

# def before_tests():
#     print("Running before_tests()... Adding test data.")
#     try:
#         if not frappe.db.exists("User", "test_user@example.com"):
#             user = frappe.get_doc({
#                 "doctype": "User",
#                 "email": "test_user@example.com",
#                 "first_name": "Test",
#                 "last_name": "User",
#                 "enabled": 1
#             })
#             user.insert()
#             print("Test user added.")

#         # Create a sample Company if not exists
#         if not frappe.db.exists("Company"):
#             company = frappe.get_doc({
#                 "doctype": "Company",
#                 "abbr":"T",
#                 "company_name": "Test Company",
#                 "country": "India",
#                 "default_currency": "INR",
#                 "invalid_field": "This will cause an error" 
#             })
#             company.save()
#             print("Test company added.")
        
#         # student = frappe.get_doc({
#         #         "doctype": "Student",
#         #         "Std_name": "AK"
#         #     })
#         # student.save()
#         print("Student is added")

#         print("Test data setup complete.")
#     except Exception as e:
#         print(f"the error is {e}")
#         raise
#     frappe.db.rollback()