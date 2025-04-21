import frappe
from frappe import _

@frappe.whitelist() 
def create_student():
    try:
        data = frappe.request.get_json()  

        student = frappe.new_doc("Student")
        student.std_id = data.get("std_id")
        student.std_name = data.get("std_name")
        student.dob = data.get("dob")
        student.gender = data.get("gender")
        student.en_roll_date = data.get("en_roll_date")
        student.subjects = data.get("subjects", [])

        for sub in data.get("subjects",[]):
            student.append("subjects", {
                sub.sub_name: data.get("sub_name"),
                sub.marks: data.get("marks")
            })
        student.insert()
        return {"status": "success", "message": "Student record created", "student_name": student.name}

    except Exception as e:
        frappe.log_error(f"Student API Error: {str(e)}")
        return {"status": "error", "message": str(e)}

@frappe.whitelist()
def get_customers_by_group():
    try:
        data = frappe.request.get_json()

        customers = frappe.db.get_list(
            "Customer",
            filters={"customer_group": data.get("customer_group")},
            fields=["name", "customer_name", "customer_group"],
            order_by="customer_name ASC"
        )

        return {"status": "success", "data": customers}

    except Exception as e:
        return {"status": "error", "message": f"Unexpected Error: {str(e)}"}

@frappe.whitelist()
def notify_me():
    frappe.msgprint("Notified")

@frappe.whitelist()
def long_task():
    frappe.msgprint("This is log task")