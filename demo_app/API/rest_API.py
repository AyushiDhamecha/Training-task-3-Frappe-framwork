# import frappe
# import json
# import requests

# base_url = "http://192.168.1.32:8001"

# headers = {
   
#     "Authorization":"token fa0e68f2b101e9b:64047c73110c428"
# }

# doc_type = "User"
# response = requests.get(f"{base_url}/api/resource/{doc_type}",headers=headers)

# if response.status_code == 200:
#     print(response.json())
# else:
#     print("Failed to fetch data")

# import frappe
# import requests

# @frappe.whitelist(allow_guest=True)
# def fetch_users():
#     base_url = frappe.utils.get_url()  # e.g., http://127.0.0.1:8000
#     headers = {
#         "Authorization": "token fa0e68f2b101e9b:64047c73110c428"
#     }
#     doc_type = "User"
#     response = requests.get(f"{base_url}/api/resource/{doc_type}", headers=headers)
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         frappe.throw(f"Failed to fetch data: {response.status_code} - {response.text}")


import frappe

@frappe.whitelist(allow_guest=True)
def get_student(first_name):
    student = frappe.get_doc("Demo_Client", first_name)
    return student.as_dict()