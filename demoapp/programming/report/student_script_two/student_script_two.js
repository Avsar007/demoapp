// Copyright (c) 2025, AK and contributors
// For license information, please see license.txt

frappe.query_reports["Student Script two"] = {
	"filters": [
		{
			"fieldname": "report_type",
			"label": __('Report Type'),
			"fieldtype": "Select",
			"options": "\nStudent Wise\nSubject Wise",
			"default": "Student Wise"
		},
		{
			"fieldname": "name",
			"label": __('Student'),
			"fieldtype": "Link",
			"options": "Student",
			"depends_on": "eval: doc.report_type == 'Student Wise'"
		},
		{
			"fieldname": "sub_name",
			"label": __('Subject'),
			"fieldtype": "Link",
			"options": "Subject Name",
			"depends_on": "eval: doc.report_type == 'Subject Wise'"
		}
	]
};
