// Copyright (c) 2025, AK and contributors
// For license information, please see license.txt

frappe.query_reports["Purchase Order 1"] = {
	"filters": [
		{
			fieldname: "from_date",
			label: __("From Date"),
			fieldtype: "Date",
			width: "80",
			reqd: 1,
			default: frappe.datetime.add_months(frappe.datetime.get_today(), -1),
		},
		{
			fieldname: "to_date",
			label: __("To Date"),
			fieldtype: "Date",
			width: "80",
			reqd: 1,
			default: frappe.datetime.get_today(),
		},
		{
			fieldname: "name",
			label: __("Purchase Order"),
			fieldtype: "Link",
			width: "80",
			options: "Purchase Order",
			get_query: () => {
				return {
					filters: { docstatus: 1 },
				};
			},
		},
		{
			fieldname: "status",
			label: __("Status"),
			fieldtype: "MultiSelectList",
			width: "80",
			get_data: function (txt) {
				let status = ["To Bill", "To Receive", "To Receive and Bill", "Completed"];
				let options = [];
				for (let option of status) {
					options.push({
						value: option,
						label: __(option),
						description: "",
					});
				}
				return options;
			},
		},
		{
			fieldname: "item_name",
			label: __("Item Description"),
			fieldtype: "Link",
			options: "Item",
			width: "100",
		},
		{
			fieldname: "supplier",
			label: __("Supplier"),
			fieldtype: "Link",
			options: "Supplier",
			width: "100"
		},
		{
			fieldname: "purchase_receipt",
			label: __("Purchase Receipt"),
			fieldtype: "Link",
			options: "Purchase Receipt",
			width: "100"
		},
		{
			fieldname: "purchase_invoice",
			label: __("Purchase Invoice"),
			fieldtype: "Link",
			options: "Purchase Invoice",
			width: "100"
		}
	],
	formatter: function (value, row, column, data, default_formatter) {
        value = default_formatter(value, row, column, data);

        if (column.fieldname === "inward_receipt_qty" && data[column.fieldname] > 0) {
            value = `<span style='color:green;font-weight:bold'>${value}</span>`;
        }

        if (column.fieldname === "qty" && data[column.fieldname] > 0) {
            value = `<span style='color:blue'>${value}</span>`;
        }
        return value;
	},
	// onload: function () {
    //     const style = document.createElement("style");
    //     style.innerHTML = `
    //         .freeze-left {
    //             position: sticky;
    //             left: 0;
    //             background: white;
    //             z-index: 100;
    //             border-right: 1px solid #ccc;
    //         }
    //     `;
    //     document.head.appendChild(style);

    //     frappe.after_ajax(() => {
    //         const interval = setInterval(() => {
    //             const firstColumnCells = document.querySelectorAll(
    //                 ".dt-scrollable .dt-cell:nth-child(2)"
    //             );
    //             if (firstColumnCells.length > 0) {
    //                 firstColumnCells.forEach(cell => {
    //                     cell.classList.add("freeze-left");
    //                 });
    //                 clearInterval(interval);
    //             }
    //         }, 500);
    //     });
    // }
	"onload": function(report) {
        report.wrapper.on('rendered', function() {
            if ($.fn.DataTable.isDataTable('#report-table')) {
                $('#report-table').DataTable().destroy();
            }

            $('#report-table').DataTable({
                scrollX: true,
                scrollY: '300px',
                scrollCollapse: true,
                paging: false,
                fixedColumns: {
                    leftColumns: 2
                }
            });
        });
    }
};

