# event_management/api.py

import frappe

def assign_role_to_user(doc, method):
    # Definisikan role yang ingin ditambahkan
    doc.role_profile_name = "Member"
    doc.save(ignore_permissions=True)
