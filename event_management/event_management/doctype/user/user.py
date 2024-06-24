import frappe
from frappe.utils import random_string

@frappe.whitelist(allow_guest=True)
def create_user(email, first_name, last_name, password):
    # Generate username
    username = email.split('@')[0]
    
    # Create new User document
    user = frappe.get_doc({
        'doctype': 'User',
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
        'send_welcome_email': 0,  # Do not send welcome email
        'new_password': password,
        'enabled': 1  # Activate the user
    })
    
    try:
        # Insert the user document into the database
        user.insert(ignore_permissions=True)
        
        # Assign default roles to the new user
        default_roles = ['Guest']  # Replace 'Guest' with any default role you prefer
        for role in default_roles:
            user.add_roles(role)
        
        return {'message': 'ok'}
    except frappe.DuplicateEntryError:
        return {'message': 'duplicate'}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), 'Create User Failed')
        return {'message': 'error'}
