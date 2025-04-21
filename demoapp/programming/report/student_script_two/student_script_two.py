# Copyright (c) 2025, AK and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint

def execute(filters=None):
    if not filters:
        filters = {}

    data, columns = [], []
    columns = get_columns(filters)
    cs_data = get_cs_data(filters)

    if not cs_data:
        msgprint(_('No Records found'))
        return columns, cs_data

    for d in cs_data:
        row = frappe._dict(d)
        data.append(row)

    return columns, data, None

def get_columns(filters):
    columns = [
        {
            "fieldname": "std_id",
            "label": _('Student ID'),
            "fieldtype": "Data",
        },
        {
            "fieldname": "std_name",
            "label": _('Student Name'),
            "fieldtype": "Data"
        },
        {
            "fieldname": "dob",
            "label": _('DOB'),
            "fieldtype": "Date"
        },
        {
            "fieldname": "gender",
            "label": _('Gender'),
            "fieldtype": "Data"
        },
        {
            "fieldname": "en_roll_date",
            "label": _('Enrollment Date'),
            "fieldtype": "Date"
        }
    ]

    if filters.get("report_type") == "Subject Wise":
        columns.extend([
            {
                "fieldname": "sub_name",
                "label": _('Subject'),
                "fieldtype": "Data"
            },
            {
                "fieldname": "marks",
                "label": _('Marks'),
                "fieldtype": "Float"
            }
        ])
    else:
        columns.extend([
            {
                "fieldname": "grade",
                "label": _('Grade'),
                "fieldtype": "Data"
            },
            {
                "fieldname": "percentage",
                "label": _('Percentage'),
                "fieldtype": "Percent"
            },
            {
                "fieldname": "status",
                "label": _('Status'),
                "fieldtype": "Text"
            }
        ])

    return columns

def get_cs_data(filters):    
    conditions = get_conditions(filters)
    
    if filters.get("report_type") == "Subject Wise":
        query = """
            SELECT 
                s.std_id, s.std_name, s.dob, s.gender, s.en_roll_date, 
                sub.sub_name, sub.marks
            FROM `tabStudent` s
            JOIN `tabSubjects` sub ON s.name = sub.parent
            {conditions}
            ORDER BY s.std_id DESC
        """.format(conditions=get_sql_conditions(filters))
        
        data = frappe.db.sql(query, as_dict=True)
    
    else: 
        data = frappe.get_all(
            "Student",
            fields=["name", "std_id", "std_name", "dob", "gender", "en_roll_date", "grade", "percentage", "status"],
            filters=conditions,
            order_by="std_id desc"
        )

    return data

def get_conditions(filters):    
    conditions = {}
    if filters.get("name"):
        conditions["name"] = filters.get("name")
    if filters.get("std_id"):
        conditions["std_id"] = filters.get("std_id")
    if filters.get("gender"):
        conditions["gender"] = filters.get("gender")
    if filters.get("en_roll_date"):
        conditions["en_roll_date"] = filters.get("en_roll_date")

    return conditions

def get_sql_conditions(filters):    
    conditions = []
    
    if filters.get("name"):
        conditions.append(f"s.name = '{filters.get('name')}'")
    if filters.get("std_id"):
        conditions.append(f"s.std_id = {filters.get('std_id')}")
    if filters.get("gender"):
        conditions.append(f"s.gender = '{filters.get('gender')}'")
    if filters.get("en_roll_date"):
        conditions.append(f"s.en_roll_date = '{filters.get('en_roll_date')}'")
    if filters.get("sub_name"):
        conditions.append(f"sub.sub_name = '{filters.get('sub_name')}'")

    return "WHERE " + " AND ".join(conditions) if conditions else ""
