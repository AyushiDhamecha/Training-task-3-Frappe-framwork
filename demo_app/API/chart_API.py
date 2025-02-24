import frappe
from frappe import _
import random
import time

@frappe.whitelist()
# def publish_realtime_chart():
#     """Publishes data to the frontend in real-time"""
#     for i in range(10):  # Sends 10 updates
#         data = {
#             "label": i,
#             "points": [random.randint(10, 100)]
#         }
#         frappe.publish_realtime("test_event", data)
#         time.sleep(2)  # Simulate real-time updates

def get_chart_data():
    # Sample data retrieval logic
    data = frappe.db.get_list('Sales Order',
        fields=['creation as date', 'grand_total as total'],
        order_by='creation asc'
    )

    # Processing data to fit chart format
    labels = [entry.date.strftime('%Y-%m-%d') for entry in data]
    values = [entry.total for entry in data]

    return {
        'labels': labels,
        'datasets': [
            {
                'name': _('Sales Orders'),  # Dataset name for the chart legend
                'values': values
            }
        ]
    }
