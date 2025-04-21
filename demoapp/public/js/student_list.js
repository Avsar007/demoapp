frappe.listview_settings['Student'] = {
    add_fields: ["status"],  // Ensure 'status' is fetched and shown
    get_indicator: function (doc) {
        if (doc.status === "Active") {
            return [__("Active"), "green", "status,=,Active"];
        } else if (doc.status === "Inactive") {
            return [__("Inactive"), "red", "status,=,Inactive"];
        }
    }
};