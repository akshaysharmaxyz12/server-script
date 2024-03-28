import frappe
from frappe.model.document import Document

class StudentDetail(Document):
    def validate(self):
        if self.checked and self.first_name and self.last_name:
            self.full_name = f"{self.first_name} {self.last_name}"

@frappe.whitelist()
def create_user_from_student(name):
    student = frappe.get_doc("Student Detail", name)
    user = frappe.new_doc("User")
    user.first_name = student.first_name
    user.last_name = student.last_name
    user.email = student.e_mail
    user.insert()
    frappe.msgprint("User created successfully.")

@frappe.whitelist(allow_guest=True)
def create_student_detail(first_name, last_name, checked=False):
    student_detail = frappe.new_doc("Student Detail")
    student_detail.first_name = first_name
    student_detail.last_name = last_name
    student_detail.checked = checked
    student_detail.insert()
    return _("Student Detail created successfully.")

@frappe.whitelist(allow_guest=True)
def get_student_detail(student_detail_name):
    return frappe.get_doc("Student Detail", student_detail_name).as_dict()

@frappe.whitelist(allow_guest=True)
def update_student_detail(student_detail_name, first_name=None, last_name=None, checked=None):
    student_detail = frappe.get_doc("Student Detail", student_detail_name)
    if first_name:
        student_detail.first_name = first_name
    if last_name:
        student_detail.last_name = last_name
    if checked is not None:
        student_detail.checked = checked
    student_detail.save()
    return _("Student Detail updated successfully.")

@frappe.whitelist(allow_guest=True)
def delete_student_detail(student_detail_name):
    frappe.delete_doc("Student Detail", student_detail_name)
    return _("Student Detail deleted successfully.")

def after_insert(doc, method):
    frappe.enqueue("server.my_project.doctype.student_detail.student_detail.create_student_detail", doc=doc.name)

def on_update(doc, method):
    frappe.enqueue("server.my_project.doctype.student_detail.student_detail.update_student_detail", doc=doc.name)

def on_trash(doc, method):
    frappe.enqueue("server.my_project.doctype.student_detail.student_detail.delete_student_detail", doc=doc.name)
