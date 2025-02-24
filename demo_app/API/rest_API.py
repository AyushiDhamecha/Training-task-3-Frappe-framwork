import frappe
import json
import requests

base_url = "http://192.168.1.32:8001"

headers = {
   
    "Authorization":"token fa0e68f2b101e9b:64047c73110c428"
}

doc_type = "User"
response = requests.get(f"{base_url}/api/resource/{doc_type}",headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print("Failed to fetch data")