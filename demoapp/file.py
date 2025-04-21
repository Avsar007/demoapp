# # import frappe

# # def before_write(file_doc, content):
# #     """Runs before a file is saved to disk."""
# #     frappe.msgprint(f"Before writing file: {file_doc.file_name}, Size: {file_size} bytes")

# # def write_file(file_doc, content):
# #     """Custom file handling (Optional: Store in external storage instead of local)."""
# #     frappe.msgprint(f"Writing file: {file_doc.file_name}")

# # def delete_file(file_doc):
# #     """Runs before a file is deleted."""
# #     frappe.msgprint(f"Deleting file: {file_doc.file_name}")

# import frappe

# def before_write(file_size=None, file_doc=None):
#     """Runs before a file is written to disk."""
#     file_name = file_doc.file_name if file_doc else "Unknown File"
#     frappe.msgprint(f"Before writing file: {file_name}, Size: {file_size} bytes")
