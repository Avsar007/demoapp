# Copyright (c) 2025, AK and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	if not filters:
		return [], []
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"fieldname": "name",
			"label":'P. O. No. / Date',
			"fieldtype": "Link",
			"options":"Purchase Order",
		},
		{
			"fieldname": "supplier",
			"label":'Supplier Name',
			"fieldtype": "Link",
			"options":"Supplier"
		},
		{
			"fieldname": "description",
			"label":'Item Description',
			"fieldtype": "Link",
			"options": "Item"
		},
		{
			"fieldname": "total_qty",
			"label":'Order Qty',
			"fieldtype": "Float",
		},
		{
			"fieldname": "schedule_date",
			"label":'Delivery Schedule Date',
			"fieldtype": "Date",
		},
		{
			"fieldname": "qty",
			"label":'Delivery Schedule Qty.',
			"fieldtype": "Float",
		},
		{
			"fieldname": "purchase_receipt", 
			"label": "Purchase Receipt No", 
			"fieldtype": "Link", 
			"options": "Purchase Receipt"
		},
		{
			"fieldname": "inward_receipt_date", 
			"label": "Inward Receipt Date", 
			"fieldtype": "Date"
		},
		{
			"fieldname": "inward_receipt_qty", 
			"label": "Inward Receipt Qty", 
			"fieldtype": "Float"
		},
		{
			"fieldname": "purchase_invoice", 
			"label": "Purchase Invoice No", 
			"fieldtype": "Link", 
			"options": "Purchase Invoice"
		},
	]

def get_data(filters):
	po_filters = {"docstatus": 1}  

	if filters.get("from_date") and filters.get("to_date"):
		po_filters["transaction_date"] = ["between", [filters["from_date"], filters["to_date"]]]

	if filters.get("name"):
		po_filters["name"] = filters["name"]

	if filters.get("status"):
		po_filters["status"] = ["in", filters["status"]]

	if filters.get("supplier"):
		po_filters["supplier"] = filters["supplier"]

	data = frappe.get_all(
		"Purchase Order",
		filters=po_filters,
		fields=["name", "supplier", "total_qty"],
		order_by="name ASC"
	)
	result = []
	for po in data:
		item_filters = {"parent": po["name"]}
		if filters.get("item_name"):
			item_filters["item_code"] = filters["item_name"]

		items = frappe.get_all(
			"Purchase Order Item",
			filters=item_filters,
			fields=["item_code", "qty", "schedule_date"]
		)

		if not items:
			continue

		child_rows = []

		for item in items:
			pr_filters = {
				"purchase_order": po["name"]
			}
			if filters.get("purchase_receipt"):
				pr_filters["parent"] = filters["purchase_receipt"]

			pr_items = frappe.get_all(
				"Purchase Receipt Item",
				filters=pr_filters,
				fields=["parent","schedule_date","received_qty"]
			)

			if filters.get("purchase_receipt") and not pr_items:
				continue

			purchase_receipt = pr_items[0].parent if pr_items else ""
			inward_receipt_date = pr_items[0]["schedule_date"] if pr_items else ""
			inward_receipt_qty = pr_items[0]["received_qty"] if pr_items else 0
		
			pi_filters = {
				"purchase_order": po["name"]
			}
			if filters.get("purchase_invoice"):
				pi_filters["parent"] = filters["purchase_invoice"]

			pi_items = frappe.get_all(
				"Purchase Invoice Item",
				filters=pi_filters,
				fields=["parent"]
			)		
			if filters.get("purchase_invoice") and not pi_items:
				continue

			purchase_invoice = pi_items[0].parent if pi_items else ""

			child_rows.append({
				"name": "",
				"supplier": "",
				"total_qty": "",
				"description": item["item_code"],
				"schedule_date": item["schedule_date"],
				"qty": item["qty"],
				"purchase_receipt": purchase_receipt,
				"inward_receipt_date": inward_receipt_date,
				"inward_receipt_qty": inward_receipt_qty,
				"purchase_invoice": purchase_invoice,
				"indent": 1
			})
		if child_rows:
			result.append({
				"name": po["name"],
				"supplier": po["supplier"],
				"total_qty": po["total_qty"],
				"description": "",
				"schedule_date": "",
				"qty": "",
				"purchase_receipt": "",
				"inward_receipt_date": "",
				"inward_receipt_qty": "",
				"purchase_invoice": "",
				"indent": 0
			})
			result.extend(child_rows)

	return result