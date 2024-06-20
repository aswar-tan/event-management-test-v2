# event_management/api.py

import frappe

def assign_role_to_user(doc, method):
    # Definisikan role yang ingin ditambahkan
    role = "test"

    # Tambahkan role ke user
    if not frappe.db.exists("Has Role", {"parent": doc.name, "role": role}):
        user_role = frappe.get_doc({
            "doctype": "Has Role",
            "parent": doc.name,
            "parentfield": "roles",
            "parenttype": "User",
            "role": role
        })
        user_role.insert()
        frappe.db.commit()

