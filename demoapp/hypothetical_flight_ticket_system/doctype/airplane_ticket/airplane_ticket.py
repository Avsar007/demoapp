# Copyright (c) 2025, AK and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document


class AirplaneTicket(Document):
	def validate(self):
		total_add_ons = 0
		for add_on in self.get("add_ons"):
				# frappe.throw("Please Select Item Only once")
			total_add_ons = total_add_ons + add_on.amount
		total_add_ons = total_add_ons + self.flight_price
		self.total_amount = total_add_ons
		self.remove_duplicate_add_ons()
		flight = frappe.get_doc("Airplane Flight", self.flight)
		airplane = frappe.get_doc("Airplane", flight.airplane)
			
		total_tickets = frappe.db.count("Airplane Ticket", {"flight": self.flight})
		if total_tickets >= airplane.capacity:
			frappe.throw("Cannot create ticket: Airplane capacity exceeded.")
	
	def remove_duplicate_add_ons(self):
		seen_items = set()
		for row in self.get("add_ons"):
			if row.item in seen_items:
				frappe.throw(f"Item '{row.item}' is already selected in Add-ons.")
			seen_items.add(row.item)

	def before_submit(self):
		if not self.status == "Boarded":
			frappe.throw("You can not submit document until board")

	def before_insert(self):
		number = random.randint(1, 99)
		letter = random.choice(['A', 'B', 'C', 'D', 'E'])
		self.seat = f"{number}{letter}"
