// Copyright (c) 2025, AK and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh: function(frm) {
        frm.add_custom_button('Assign Seat', () => {
            frappe.prompt([
                {
                    label: 'Seat Number',
                    fieldname: 'seat',
                    fieldtype: 'Data'
                }
            ], (values) => {
                frm.set_value('seat', values.seat);
                frm.save();
            }, 'Selects Seat','Assign');
        },'Actions');
	},
});
