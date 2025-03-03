import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_document(doctype):
       
        return frappe.db.get_list(doctype)


