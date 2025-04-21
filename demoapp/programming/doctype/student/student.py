# Copyright (c) 2025, AK and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student(Document):
    def validate(self):
        self.calculate_percentage()
        self.grade_calculation()
        self.update_student_status()
        self.check()
        # self.ensure_dob_less_erroll()
        # self.error_handling()
        # self.add_comment("Shared",f"{frappe.session.user}This is the change")
    
    # Understanding of realtime and enqueue envents in deep.......................................................

        # frappe.enqueue(self.long_running_job, queue ='short', is_async=True ,params1 = self.std_id, params2 = self.std_name)
        # self.doc_second_fetch_realtime()
        
    # def on_update(self):
    #     self.doc_fetch_realtime()    

# Document API's..............................................................

    # def before_save(self):      
    #     self.update_student_name(self.std_id,self.std_name)
    
    # def update_student_name(self,std_id, new_name):
    #     if frappe.db.exists("Student", {"std_id": std_id}):
    #         frappe.db.set_value("Student", "STD-001", "std_name", new_name)
    #         frappe.db.commit()
    #         frappe.msgprint(f"Student {std_id} name updated to {new_name}")
    #     else:
    #         frappe.msgprint("Student does not exist!")


    # Claculate Percentage ..................................................................
    def calculate_percentage(self):
        total_marks = 0
        total_subjects = len(self.subjects)  

        if total_subjects == 0:
            self.percentage = 0.00
            return

        for subject in self.subjects:
            total_marks += subject.marks  

        max_marks = 100  
        max_total_marks = total_subjects * max_marks
        self.percentage = (total_marks / max_total_marks) * 100

        # Grade Calculation .....................................................................................

    def grade_calculation(self):
        if self.percentage >= 90:
            self.grade = "A+"
        elif self.percentage >= 80:
            self.grade = "A"
        elif self.percentage >= 70:
            self.grade = "B"
        elif self.percentage >= 60:
            self.grade = "C"
        else:
            self.grade = "F"

    def update_student_status(self):
        if self.percentage >= 50:
            self.status = "Excellent Performance, Congratulations!"
        elif self.percentage >= 33:
            self.status = "Congrats! Pass, Increase Your Performance"
        else:
            self.status = "Failed! Better Luck Next Time"
   

        # Show progress-line .................................................................................................
 
        # frappe.publish_progress(100, title='Some title', description='Some description')


    # Understanding of realtime and enqueue envents in deep.......................................................

    # def long_running_job(self, params1, params2):
    #     frappe.publish_realtime('show_popup', {'message': f"{params1}, {params2}"})  

    # def doc_fetch_realtime(self):
    #     old_student = self.get_doc_before_save()
    #     # title = student.get_title()
    #     frappe.publish_realtime('doc_fetch', {'message': f'Hello {old_student.std_name},{self.std_name} from first Event'})
    #     # if student.check_permission(permtype = "read"):
    #     # else:
    #     #     frappe.throw(f"{title} You don't have permission for read this doc")

    # def doc_second_fetch_realtime(self):
    #     url = self.get_url()
    #    `frappe.publish_realtime('doc_second_fetch', {'message': f"{url} Hello from secont Event"})

    # def check(self):
    #     for subject in self.subjects:
    #         frappe.msgprint(f"{self.std_name} have {subject.marks} marks in {subject.sub_name}")

    # def check(self):
    #     subjects = frappe.get_all("Subjects",
    #                                filters={
    #                                     "parenttype": "Student",
    #                                     "parentfield": "subjects"
    #                                 },
    #                                 fields=["name","sub_name","marks","creation","modified_by"]
    #                                 )
    #     print("\n\n\n")
    #     for subject in subjects:
    #         print(f"\n{subject}")
    #     print("\n\n\n")

    def check(self):
        subjects = frappe.get_list("Subjects",
                                   filters={
                                        "parenttype": "Student",
                                        "parentfield": "subjects"
                                    },
                                    fields=["name","sub_name","marks","creation","modified_by"]
                                    )
        print("\n\n\n")
        for subject in subjects:
            print(f"\n{subject}")
        print("\n\n\n")

    def ensure_dob_less_erroll(self):
        if self.dob > self.en_roll_date:
            frappe.throw("You entered wrong date")


@frappe.whitelist()
def create_or_update_employee(student_name, dob, doj, gender):

    employee = frappe.new_doc("Employee")

    employee.first_name = student_name
    employee.date_of_birth = dob
    employee.date_of_joining = doj
    employee.gender = gender
    employee.save()
    
    frappe.db.set_value("Student", {"std_name": student_name},"employee",employee.name)
    frappe.db.commit()
    

    return f"Employee is created"

    
