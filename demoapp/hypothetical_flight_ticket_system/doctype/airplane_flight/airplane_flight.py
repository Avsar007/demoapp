# Copyright (c) 2025, AK and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.status = "Completed"
	def before_save(self):
	    self.route = f"{self.airplane.lower().replace(' ', '-')}-{self.source_airport_code.lower()}-{self.destination_airport_code.lower()}"