# Copyright (c) 2024, akshay sharma and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe



@frappe.whitelist(allow_guest=True)
def get_users():
    users = frappe.get_all("User", fields=["name", "first_name", "last_name", "email"])
    return users

# @frappe.whitelist(allow_guest=True)
# def create_user_from_student(first_name, last_name, email):
#         # Check if the user already exists with the given email
#         if frappe.db.exists("User", {"email": email}):
#             frappe.msgprint(f"User with email {email} already exists.")
#             return

#         # Create a new User document
#         user = frappe.new_doc("User")
#         user.first_name = first_name
#         user.last_name = last_name
#         user.email = email
#         user.insert(ignore_permissions=True)
#         frappe.msgprint("User created successfully.")
    

@frappe.whitelist(allow_guest=True)
def create_user_from_student(first_name, last_name, email):
    try:
        # Check if the user already exists with the given email
        if frappe.db.exists("User", {"email": email}):
            frappe.msgprint(f"User with email {email} already exists.")
            return

        # Create a new User document
        user = frappe.new_doc("User")
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.insert(ignore_permissions=True)
        frappe.msgprint("User created successfully.")
    except Exception as e:
        frappe.log_error(f"Error creating user: {e}")
        frappe.throw("Failed to create user. Please check logs for details.")


