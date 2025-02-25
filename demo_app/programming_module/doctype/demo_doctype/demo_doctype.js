// Copyright (c) 2025, asd and contributors
// For license information, please see license.txt

frappe.ui.form.on("Demo Doctype", {
	refresh: function(frm) {
        frm.add_custom_button(__('Open Dialog'), function() {
            let d = new frappe.ui.Dialog({
                title: 'Enter Student Details',
                fields: [
                    {
                        label: 'Student Name',
                        fieldname: 'student_name',
                        fieldtype: 'Data'
                    },
                    {
                        label: 'Age',
                        fieldname: 'age',
                        fieldtype: 'Int'
                    },
                    {
                        label: 'Email',
                        fieldname: 'email',
                        fieldtype: 'Data'
                    }
                ],
                primary_action_label: 'Submit',
                primary_action(values) {
                    frappe.call({
                        method: 'demo_app.programming_module.doctype.student_doc.student_doc.new_document',
                        args: values,
                        callback: function(response) {
                            frappe.msgprint('Student Saved Successfully!');
                            d.hide();
                        }
                    }); 
                }
            });

            d.show();
        });
    }
});
