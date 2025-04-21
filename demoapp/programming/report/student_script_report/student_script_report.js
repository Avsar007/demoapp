	// Copyright (c) 2025, AK and contributors
	// For license information, please see license.txt

	frappe.query_reports["Student Script Report"] = {
		"filters": [
			{
				"fieldname": "name",
				"label":__('Student'),
				"fieldtype": "Link",
				"options" : "Student"
			},
			{
				"fieldname": "std_id",
				"label":__('Student ID'),
				"fieldtype": "Data",
			},
			{
				"fieldname": "std_name",
				"label":__('Student Name'),
				"fieldtype": "Data"
			},
			{
				"fieldname": "sub_name",
				"label":__('Subjects'),
				"fieldtype": "Link",
				"options": "Subject Name",
			},
			// {
			// 	"fieldname": "dob",
			// 	"label":__('DOB'),
			// 	"fieldtype": "Date"
			// },
			{
				"fieldname": "gender",
				"label":__('Gender'),
				"fieldtype": "Link",
				"options": "Gender"
			},
			{
				"fieldname": "en_roll_date",
				"label":__('Enroll Date'),
				"fieldtype": "Date",
			},
			// {
			// 	"fieldname": "grade",
			// 	"label":__('Grade'),
			// 	"fieldtype": "Data"
			// },
			// {
			// 	"fieldname": "percentage",
			// 	"label":__('Percentage'),
			// 	"fieldtype": "Percent"
			// },
			// {
			// 	"fieldname": "status_notes",
			// 	"label":__('Status Notes'),
			// 	"fieldtype": "Text"
			// },
		]
	};
