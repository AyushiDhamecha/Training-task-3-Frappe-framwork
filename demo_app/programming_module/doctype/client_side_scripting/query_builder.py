import frappe
from frappe.query_builder import DocType

# def get_client_data():
#     CliertSide = DocType("Client Side Scripting")
#     query = (
#         frappe.qb.from_(CliertSide)
#         .select(CliertSide.first_name, CliertSide.full_name, CliertSide.age)
#     )
#     return query.run(as_dict=True)

def get_student_data():
    student = DocType("Student Doc")
    query = (
        frappe.qb.from_(student)
        .select(student.student_name, student.age, student.email)
        .where(student.age  >= 22)
    )
    return query.run(as_dict=True)