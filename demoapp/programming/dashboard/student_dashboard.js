frappe.provide("demoapp.student");

demoapp.student.show_student_stats = function () {
    const dialog = new frappe.ui.Dialog({
        title: __("Student Summary"),
        fields: [
            {
                label: __("Total Students"),
                fieldname: "student_count",
                fieldtype: "Int",
                read_only: 1,
            },
        ],
    });

    frappe.db.count("Student").then((count) => {
        dialog.get_field("student_count").set_value(count);
    });

    dialog.show();
};
