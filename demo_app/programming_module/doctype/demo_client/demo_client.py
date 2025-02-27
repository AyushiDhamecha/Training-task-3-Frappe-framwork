# # Copyright (c) 2025, asd and contributors
# # For license information, please see license.txt

# import frappe
# from frappe.website.website_generator import WebsiteGenerator
# from frappe.model.naming import getseries
# from frappe.model.naming import make_autoname  # Ensure import

# class Demo_Client(WebsiteGenerator):
# 	def autoname(self):
# 		# select a project name based on customer
# 		prefix = "P-{}-".format(self.first_name)
# 		self.name = getseries(prefix, 3)
	
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import make_autoname  # Ensure import

class Demo_Client(WebsiteGenerator):
    pass
    # def autoname(self):
    #     if not self.first_name:
    #         frappe.throw("First Name is required for naming!")

    #     prefix = "P-{}-".format(self.first_name)
    #     self.name = make_autoname(prefix + ".###")




