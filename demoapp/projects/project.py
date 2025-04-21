def get_context(context):
    project_name = frappe.form_dict.name
    project = frappe.get_doc("Project", project_name)
    context.project = project