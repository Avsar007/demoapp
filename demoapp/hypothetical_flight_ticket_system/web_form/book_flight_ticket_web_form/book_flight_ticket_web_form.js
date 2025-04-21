frappe.ready(function() {
	// bind events here
})

frappe.web_form.after_load = () => {
    const urlParams = new URLSearchParams(window.location.search);
    const flight = urlParams.get('flight');

    if (flight) {
        // Set flight value
        frappe.web_form.set_value('flight', flight);

        // You can use custom logic or static values for flight_price
        // Example static value
        const default_price = 11000;
        frappe.web_form.set_value('flight_price', default_price);
    }
};
