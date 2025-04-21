from frappe import _


def get_data():
	return {
		"heatmap": True,
		"heatmap_message": _("This is based on Student Entery. See {0} for details").format(
			'<a href="/app/query-report/Student Script two">' + _("Student Script two") + "</a>"
		),
		"transactions": [
			{"label": _("Related"), "items": ["Employee", "Subject Name"]},
		],
	}
