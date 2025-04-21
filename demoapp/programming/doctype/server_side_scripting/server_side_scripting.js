// Copyright (c) 2025, AK and contributors
// For license information, please see license.txt

frappe.ui.form.on("Server Side Scripting", {
	enable: function (frm) {
        // frm.call({
        //     doc : frm.doc,
        //     method : 'frm_call',
        //     args : {
        //         msg : "Hello"
        //     },
        //     freeze : true,
        //     freeze_message : __("Calling frm_call method"),
        //     callback : function(r){
        //         frappe.msgprint(r.message)
        //     }
        // });
        // frappe.call({
        //     method : 'demoapp.programming.doctype.client_side_scripting.client_side_scripting.frappe_call',
        //     args : {
        //         msg : "Hello"
        //     },
        //     freeze : true,
        //     freeze_message : "calling frappe_call method",
        //     callback : function(r){
        //         frappe.msgprint(r.message)
        //     }
        // });
	},
});
