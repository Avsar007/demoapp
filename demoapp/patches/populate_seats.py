import frappe
import random

def execute():
    # Fetch all tickets with empty seat values
    tickets = frappe.get_all("Airplane Ticket", filters={"seat": ["is", "not set"]}, fields=["name"])

    for ticket in tickets:
        seat_number = random.randint(1, 99)
        seat_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        seat = f"{seat_number}{seat_letter}"

        # Update the seat value
        frappe.db.set_value("Airplane Ticket", ticket.name, "seat", seat)

    frappe.db.commit()  # commit manually as patches run outside standard form context
