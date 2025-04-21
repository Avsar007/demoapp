# Copyright (c) 2025, AK and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint

def execute(filters=None):
	if not filters: filters = {}

	data, columns = [], []

	columns = get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data:
		msgprint(_('No Records found'))
		return columns, cs_data
	
	# data = []
	for d in cs_data:
		row = frappe._dict({
			'std_id': d.std_id,
			'std_name': d.std_name,
			'dob': d.dob,
			'gender': d.gender,
			'en_roll_date': d.en_roll_date,
			# 'subjects': d.subjects,	
			'grade': d.grade,
			'percentage': d.percentage,
			'status_notes': d.status_notes
		})
		data.append(row)

	chart = get_chart_data(data)
	report_summary = get_report_summury(data)
	return columns, data, None, chart, report_summary

def get_columns():
	return [
		{
			"fieldname": "std_id",
			"label":_('Student ID'),
			"fieldtype": "Data",
		},
		{
			"fieldname": "std_name",
			"label":_('Name'),
			"fieldtype": "Data"
		},
		{
			"fieldname": "dob",
			"label":_('DOB'),
			"fieldtype": "Date"
		},
		{
			"fieldname": "gender",
			"label":_('Gender'),
			"fieldtype": "Link",
			"options": "Gender"
		},
		{
			"fieldname": "en_roll_date",
			"label":_('En. Roll. Date'),
			"fieldtype": "Date",
		},
		# {
		# 	"fieldname": "subjects",
		# 	"label":_('Subjects'),
		# 	"fieldtype": "Data",
		# },
		{
			"fieldname": "grade",
			"label":_('Grade'),
			"fieldtype": "Data"
		},
		{
			"fieldname": "percentage",
			"label":_('Percentage'),
			"fieldtype": "Percent"
		},
		{
			"fieldname": "status_notes",
			"label":_('Status'),
			"fieldtype": "Text"
		},
	]

def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype='Student',
		fields=['name','std_id','std_name','dob','gender','en_roll_date','grade','percentage','status_notes'],
		filters=conditions,
		order_by='std_id desc'
	)	
	# data = []
	
	# for student in students:
	# 	student_doc = frappe.get_doc("Student", student.name)
	# 	if student_doc.get("subjects"):
	# 		for sub in student_doc.get("subjects"):  # Loop through child table
	# 			row = {
    #                 'id': student.name,  # Unique ID (name)
    #                 'std_id': student.std_id,
    #                 'std_name': student.std_name,
    #                 'sub_name': sub.sub_name,  # Subject Name from child table
    #                 'marks': sub.marks,   # Marks from child table
    #                 'percentage': student.percentage,
    #                 'grade': student.grade,
    #                 'status_notes': student.status_notes
    #             }
	# 			data.append(row)
	# 	else:
	# 		row = {
    #             'id': student.name,
    #             'std_id': student.std_id,
    #             'std_name': student.std_name,
    #             'sub_name': "No Subjects",
    #             'marks': "-",
    #             'percentage': student.percentage,
    #             'grade': student.grade,
    #             'status_notes': student.status_notes
	# 		}
	# 		data.append(row)	
	return data

def get_conditions(filters):
	conditions = {}
	for key,value in filters.items():
		if filters.get(key):
			conditions[key] = value
	return conditions

def get_chart_data(data):
	if not data:
		return None
	labels = ['Percentage <= 80','Percentage > 80']

	percentage_data = {
		'Percentage <= 80': 0,
		'Percentage > 80': 0,
	}
	datasets = []

	for entry in data:
		if entry.percentage <= 80:
			percentage_data['Percentage <= 80'] += 1

		else:
			percentage_data['Percentage > 80'] += 1

	datasets.append({
		'name': 'Persentage',
		'values': [percentage_data.get('Percentage <= 80'),percentage_data.get('Percentage > 80')]
	})

	chart = {
		'data': {
			'labels': labels,
			'datasets': datasets
		},
		'type': 'line',
		'height': 300,
	}
		
	return chart

def get_report_summury(data):
	if not data:
		return None
	
	percentage_below_80, percentage_above_80 = 0, 0

	for entry in data:
		if entry.percentage <= 80:
			percentage_below_80 += 1
		else:
			percentage_above_80 += 1
	return [
		{
			'value': percentage_below_80,
			'indicator': 'Green',
			'label': 'percentage Below 80%',
			'datatype': 'Int'
		},
		{
			'value': percentage_above_80,
			'indicator': 'Red',
			'label': 'percentage Above 80%',
			'datatype': 'Int'
		},
	]