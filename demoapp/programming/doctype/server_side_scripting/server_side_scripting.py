# Copyright (c) 2025, AK and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import time

class ServerSideScripting(Document):
    pass
	# # def validate(self):
	# 	try:
	# 		frappe.db.savepoint("before_insert")  # Create a savepoint
	# 		doc = frappe.get_doc({
    # 		    "doctype": "Customer",
    # 		    "customer_name": "John Doe",
    # 		})
	# 		doc.insert()
    
    # 		# Force an error (e.g., invalid SQL)
	# 		frappe.db.sql("INVALID SQL SYNTAX")
			
	# 		frappe.db.commit()  # Commit if everything is successful

	# 	except Exception as e:
	# 		frappe.db.rollback(save_point="before_insert")  # Rollback to the savepoint
	# 		frappe.log_error(f"Error: {str(e)}", "Transaction Error")
	# # 	frappe.msgprint("Hello Frappe from 'validate' Event "f"{self.first_name} {self.last_name}")	
		 



    # def before_save(self):
    #     frappe.throw("Hello frappe from 'befor_save' Event")
        
	# def before_insert(self):
	# 	frappe.msgprint("Hello from before insert")

	# def after_insert(self):
	# 	frappe.msgprint("Hello from after_save")

	# def on_update(self):
	# 	frappe.throw("Hello from on update")
    
	# def before_submit(self):
	# 	frappe.msgprint("Hello from before submit")

	# def on_submit(self):
	# 	frappe.msgprint("Hello from on Submit")

	# def on_cancel(self):
	# 	frappe.msgprint("Hello from on cancel")

	# def on_trash(self):
	# 	frappe.msgprint("Hello from on trash")

	# def after_delete(self):
	# 	frappe.msgprint('Hello from after delete')
    
	# def validate(self):
	# 	frappe.msgprint(("Hello My full name is '{0}' ").format(
	# 		self.first_name + " " + self.middle_name + " " + self.last_name))
    
	# def validate(self):
	# 	for row in self.get("family_members"):
	# 		frappe.msgprint((
	# 			"{0}. The family member name is '{1}' and relation is '{2}'").format(
	# 				row.idx,row.name1,row.relation))
    
# fetch value from other doc(interact).............................................................................
	# def validate(self):
	# 	self.get_document()

	# def get_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting',self.client_side)
	# 	frappe.msgprint(("The first Name is {0} and Age is {1}").format(doc.first_name,doc.age))

	# 	for row in doc.family_members: #here doc.get("family_members") also works #and if we need current docType's child data so use self.fieldname of child link
	# 		frappe.msgprint(("{0} The family member name is {1} and Age is {2}. The relation is {3}").format(row.idx,row.name1,row.age,row.relation))

# Create a Document using new_doc method....................................................
	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = "Avsar"
	# 	doc.last_name = "Kalola"
	# 	doc.age = 21
	# 	doc.append('family_members',{
	# 		"name1" : "P",
	# 		"relation" : "Father",
	# 		"age" : 49
	# 	})
	# # 	# doc1 = frappe.new_doc('Server Side Scripting')
	# # 	# doc1.append('family_members',{
	# # 	# 	"name1" : "P",
	# # 	# 	"relation" : "Father",
	# # 	# 	"age" : 49
	# # 	# })
	# # 	# doc1.insert()
	# 	doc.insert(
	# 		# ignore_permissions = True,
	# 		# ignore_links = True,
	# 		# ignore_if_duplicate = True,
	# 		ignore_mandatory = True
	# 	)

# delete a document usinf delete_doc method..............................................................
	# def validate(self):
	# 	frappe.delete_doc('Client Side Scripting','PR-0018')

# doc.save()............................................................................
	# def validate(self):
	# 	self.save_document()

	# def save_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting','PR-0021')
	# 	doc.first_name = "AK"
	# 	doc.save()

# doc.delete()..........................................................................
	# def validate(self):
	# 	doc = frappe.get_doc('Client Side Scripting','PR-0019')
	# 	doc.delete()

# doc.db_set()..........................................................................
	# def validate(self):
	# 	self.db_set_document()

	# def db_set_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting','PR-0022')
	# 	doc.db_set("age",50)

# doc.db.get_list()......................................................................
	# def validate(self):
	# 	self.get_list()
	
	# def get_list(self):
	# 	doc = frappe.db.get_list('Client Side Scripting',
	# 		filters={
	# 			'enable' : 1
	# 		},
	# 		fields = ['first_name', 'age']
	# 	)
	# 	for d in doc:
	# 		frappe.msgprint(("The perent First name is {0} and age is {1}").format(d.first_name,d.age))

# doc.db.get_value.......................................................................,,,

	# def validate(self):
	# 	self.get_value()
	# def get_value(self):
	# 	first_name, age = frappe.db.get_value('Client Side Scripting','PR-0008',['first_name','age'])
	# 	frappe.msgprint(("The Parent First Name is {0} and age is {1}").format(first_name, age))

# doc.db.set_value.......................................................................................

	# def validate(self):
	# 	self.set_value()

	# def set_value(self):
	# 	frappe.db.set_value('Client Side Scripting','PR-0021','age',25)
	# 	first_name, age = frappe.db.get_value('Client Side Scripting','PR-0021',['first_name','age'])
	# 	frappe.msgprint(("The Parent First Name is {0} and age is {1}").format(first_name, age))

# exists() & count().......................................................................................

	# def validate(self):
	# 	if frappe.db.exists('Client Side Scripting','PR-0013'):
	# 		frappe.msgprint("The Document is Exist")
	# 	else:
	# 		frappe.msgprint("The Document Doesn't Exist")

	# def validate(self):
	# 	doc_count = frappe.db.count('Client Side Scripting',{"first_name" : "Avsar"})
	# 	frappe.msgprint(("There is {0} documents in doctype which has first_name Avsar").format(doc_count))

# frappe.db.sql()............................................................................................................
	# def validate(self):
	# 	self.sql()

	# def sql(self):
	# 	data = frappe.db.sql(
	# 		"""
	# 		SELECT first_name, age
	# 		FROM `tabClient Side Scripting`
	# 		WHERE enable = 0
	# 		"""
	# 	,as_dict = 1)

	# 	for d in data:
	# 		frappe.msgprint(("The Parent first name is {0} and age is {1}").format(d.first_name,d.age))

# # frm_call from server.............................................................................

	# @frappe.whitelist()
	# def frm_call(self,msg):
	# 	time.sleep(2)
	# 	# frappe.msgprint(msg)

	# 	# self.phone_no=9428710651
	# 	return "Hey This message from frm_call"

	