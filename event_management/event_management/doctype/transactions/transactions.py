# Copyright (c) 2024, konoha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime


class Transactions(Document):
    def before_insert(self):
        self.check_product_price()
    def check_product_price(self):
        # Ambil detail produk berdasarkan Event yang terkait dengan transaksi
        event = frappe.get_doc("Events", self.event)
        
        # Ambil kategori event
        event_category = event.category
        
        # Cek jika kategori event adalah 'gratis' atau 'Gratis'
        if event_category.lower() == 'gratis':
            self.status = 'Terkonfirmasi'
        else:
            self.status = 'Menunggu Konfirmasi'
        
        # Set pengguna yang melakukan transaksi
        self.participant = frappe.session.user
        self.date = now_datetime()
