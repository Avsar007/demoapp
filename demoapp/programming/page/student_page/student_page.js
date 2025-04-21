frappe.pages['student-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Student Page',
		single_column: true
	});
	page.set_title("Student's Page")
	page.set_indicator("Done","green")

	let $dtn = page.set_primary_action("New", () => frappe.msgprint("Clicked New"))
	let $btnOne = page.set_secondary_action("Refresh", () => frappe.msgprint("Clicked Refresh"))
	page.add_menu_item("Send Email", () => frappe.msgprint("Clicked Send Email"))
	page.add_action_item("Delete", () => frappe.msgprint("Clicked Delete"))

	let field = page.add_field({
		label: 'Status',
		fieldtype: 'Select',
		fieldname: 'Status',
		options: [
			'Open',
			'Closed',
			'Cancelled'
		],
		change() {
			frappe.msgprint(field.get_value());
		}
	});

	$(frappe.render_template("student_page",{
		data:"Hello Student"
	})).appendTo(page.body)
}