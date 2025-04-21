import frappe

@frappe.whitelist()
def get_customers_by_group():
    try:
        data = frappe.request.get_json()

        customers = frappe.db.get_list(
            "Customer",
            filters={"customer_group": data.get("customer_group")},
            fields=["name","customer_name", "customer_group"],
            order_by="customer_name ASC"
        )

        return {"status": "success", "data": customers}

    except Exception as e:
        return {"status": "error", "message": f"Unexpected Error: {str(e)}"}
