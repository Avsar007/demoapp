# Copyright (c) 2025, AK and contributors
# For license information, please see license.txt

import frappe
import time
from frappe.model.document import Document


class ClientSideScripting(Document):
	pass


# @frappe.whitelist()
# def frappe_call(msg):
# 	time.sleep(1)
# 	# frappe.msgprint(msg)
	
# # phone_no=9428710651 
# # we can't set any data in frappe_call

# 	return "Hey This message from frappe_call"
