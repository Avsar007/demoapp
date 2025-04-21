import frappe

def execute(filters=None):
    airlines = frappe.get_all("Airline", fields=["name"])
    data = []
    total = 0

    for airline in airlines:
        flight_tickets = frappe.db.get_all(
            "Airplane Ticket",
        	{"flight": ["like", f"{airline.name}%"]},
            "name"
        )
        revenue = 0
        if flight_tickets:
            for flight_ticket in flight_tickets:
                ticket_revenue = frappe.db.get_value("Airplane Ticket", flight_ticket.name, "total_amount") or 0
                revenue += ticket_revenue
        data.append([airline.name, revenue])	
        total += revenue
            

    columns = [
        {"label": "Airline", "fieldname": "airline", "fieldtype": "Link", "options": "Airline", "width": 200},
        {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency", "width": 150},
    ]

    chart = {
        "data": {
            "labels": [row[0] for row in data],
            "datasets": [{"name": "Revenue", "values": [row[1] for row in data]}]
        },
        "type": "donut"
    }

    summary = [
        {"label": "Total Revenue", "value": total, "datatype": "Currency"}
    ]

    return columns, data, None, chart, summary
