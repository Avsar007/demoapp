// Copyright (c) 2025, AK and contributors
// For license information, please see license.txt

frappe.ui.form.on("Student", {
	// after_save: function(frm) {
    //     frappe.msgprint(__("Student Name is '{0}'",[frm.doc.std_name]))
	// },
    validate: function(frm) {
        if(frm.doc.dob > frm.doc.en_roll_date){
            frappe.throw("You are not Enrolled")
        }
        select_uniq_sub(frm)
    },
    refresh: function(frm) {
        frm.add_custom_button(__('Create/Update Employee'), function() {
            frappe.call({
                method: 'demoapp.programming.doctype.student.student.create_or_update_employee',
                args: {
                    student_name: frm.doc.std_name,
                    dob: frm.doc.dob,
                    doj: frm.doc.en_roll_date,
                    gender: frm.doc.gender
                },
                callback: function(r) {
                    if (!r.exc) {
                        frappe.msgprint(r.message)
                    }
                }
            });
        });
        frappe.require('demoapp/programming/dashboard/student_dashboard.js', () => {
            frm.dashboard.add_transactions([
                {
                    label: __("Custom Actions"),
                    items: [
                        {
                            label: __("Show Student Stats"),
                            onclick: () => {
                                // Now this function is available after require
                                demoapp.student.show_student_stats();
                            }
                        }
                    ]
                }
            ]);
        });
    }
});

frappe.ui.form.on("Subjects",{
    marks: function(frm) {
        frm.set_intro("Marks must be between 0 and 100.")
        frm.doc.subjects.forEach(subject => {
            if (subject.marks < 1 || subject.marks > 100) {
                frm.set_intro("Marks must be between 0 and 100.")    
                frappe.throw(("Marks must be between 0 and 100."));
            }  
        });
        frm.set_intro("Marks must be between 0 and 100.")
        calculate_percentage(frm)
    },
    
})

function select_uniq_sub(frm) {
    let set_subject = new Set();
    
    frm.doc.subjects.forEach(subject => {
        if(subject.sub_name){
            if(set_subject.has(subject.sub_name)){
                frappe.msgprint("Please enter " + subject.sub_name + " Subject 'Only Once'");
                frappe.validated = false
                return false;
            }
            set_subject.add(subject.sub_name)
        }
    })
}

// Claculate Percentage........................................................................


function calculate_percentage(frm) {
    let total_marks = 0;
    let total_subjects = frm.doc.subjects.length;

    if (total_subjects === 0) {
        frm.set_value('persentage', 0);
        return;
    }

    frm.doc.subjects.forEach(subject => {
        total_marks += subject.marks || 0;
    });

    let max_total_marks = total_subjects * 100
    let percentage = (total_marks / max_total_marks) * 100;

    frm.set_value('percentage', percentage.toFixed(2));
}


// Understanding of realtime and enqueue in deeep...............................................................................................

// frappe.realtime.on('doc_second_fetch', function(data) {
//     console.log(data.message);
//     // frappe.msgprint(data.message)
// })

// frappe.realtime.on('show_popup',function(data) {
//     console.log(data.message);
//     // frappe.msgprint(data.message)
// });

// frappe.realtime.on('doc_fetch', function(data) {
//     console.log(data.message);
//     // frappe.msgprint(data.message);
//         // frappe.msgprint({
//         //     message: data.message,
//         //     title: "Notification",
//         //     indicator: "green",
//         // });
// });

