// Copyright (c) 2025, AK and contributors
// For license information, please see license.txt

frappe.ui.form.on("Client Side Scripting", {

    // Events........................................................

	// refresh: function(frm) {
    //     frappe.msgprint("Hello User from 'refresh' event")
    //     // frappe.throw("This is an Error")
	// }

    // onload: function(frm) {
    //     frappe.msgprint("Hello User from 'onload' event")
    // }

    // validate: function(frm) {
    //     frappe.msgprint("Hello User from 'validate' event",indicator="orange");
    // },

    // before_save: function(frm) {
    //     frappe.throw("Hello User from 'before_save' event")
    // },

    // after_save: function(frm) {
    //     frappe.throw("Hello User from 'after_save' event")
    // }

    // enable: function(frm) {
    //     frappe.msgprint("Hello User from 'enable' event")
    // },

    // age: function(frm) {
    //     frappe.msgprint("Hello User from 'age' event")
    // }

    // before_submit: function(frm) {
    //     frappe.throw("Hello User from 'before_submit' event")
    // }

    // on_submit: function(frm) {
    //     frappe.msgprint("Hello User from 'on_submit' event")
    // }

    // before_cancel: function(frm) {
    //     frappe.throw ("Hello User from 'before_cancel' event")
    // }

    // after_cancel: function(frm) {
    //     frappe.msgprint("Hello User from 'after_cancel' event")
    // }
     
    // Value Fetching...............................................................................

    // frm.doc.first_name

    // after_save: function(frm){
    //     // frappe.msgprint(__("The full name is '{0}'",
    //     //     [frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name]
    //     // ))
    //     for(let row of frm.doc.family_members) {
    //         frappe.msgprint(__("{0}. The family member name is '{1}' and relation is '{2}'",
    //             [row.idx,row.name1,row.relation]
    //         ))
    //     }
    // },

    // set_intro & is_new...........................................................

    // refresh: function(frm) {
    //     // frm.set_intro('Now you can create a new Client Side Scripting doctype')

    //     if(frm.is_new()) {
    //         frm.set_intro('Now you can created a new Client Side Scripting doctype')
    //     }
    // }

    // set_value ............................................................................................................
    // validate: function(frm) {
        // frm.set_value('full_name',frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name)

    //     let row = frm.add_child('family_members', {
    //         name1: 'Avsar Kalola',
    //         relation: 'Son',
    //         age: 21
    //     })

    //     if(!frm.doc.age){
    //         frappe.throw("age is required before saving!");
    //     }
    // }

    // set_df_property.............................................................................
    // enable: function(frm) {
    //     // frm.set_df_property('first_name','reqd',1)
    //     // frm.refresh_find('first_name');
    //     // frm.set_df_property('middle_name','read_only',1)
    //     // frm.refresh_field('middle_name');
    //     frm.toggle_reqd('age',true)
    // }

    //add_custom_button
    refresh:function (frm) {
        frm.add_custom_button('Click Me Button',() => {
            frappe.msgprint(__('You Clicked Me!'));
        })

        // frm.add_custom_button('Click Me1',() => {
        //     frappe.msgprint(__('You Clicked 1 !!'));
        // },'click me')

        // frm.add_custom_button('Click Me2',() => {
        //     frappe.msgprint(__('You Clicked 2 !!'));
        // },'click me')
    }
    // refresh: function(frm) {
    //     frm.set_df_property('full_name', 'read_only', !frm.is_new());
    // }
});

// Chiled Table Events

frappe.ui.form.on('Family Members', {
    // name1: function(frm) {
    //     frappe.msgprint("Hello User from Child DocType event")
    // },

    // age: function(frm) {
    //     frappe.msgprint("Hello User from 'age' child doctype fieldmame event")
    // }

    // name1: function(frm,cdt,cdn){
    //     let row = locals[cdt][cdn]
    //     console.log(row.name)
    // }
});