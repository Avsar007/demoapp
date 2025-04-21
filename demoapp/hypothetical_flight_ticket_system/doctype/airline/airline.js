// Copyright (c) 2025, AK and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
    refresh: function(frm) {
        const website_link = frm.doc.website;
        if (website_link) {
            frm.add_web_link(website_link, "Visit Website");
        }
    }
});
