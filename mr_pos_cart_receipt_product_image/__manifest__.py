# -*- coding: utf-8 -*-
{
    'name': 'POS Product Image on Cart, Receipt & Invoice',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Display product images on POS cart lines, printed receipt, and customer invoice PDF.',
    'description': """
POS Product Image On Cart, Receipt & Invoice
============================================

Bring your Point of Sale experience to life by showing product images
everywhere a sale is handled — cart, receipt, and invoice.

Features
--------
* **Cart** – Every order line in the POS cart shows a thumbnail of the
  product so the cashier can instantly confirm the right item.
* **Receipt** – The same product image is printed next to each line on
  the customer receipt.
* **Invoice PDF** – A product image column is added to the customer
  invoice PDF, giving professional, visually rich documents.
* **Full control** – Each location (cart, receipt, invoice) has its own
  independent on/off toggle inside Point of Sale ► Settings ► Product
  Images, so you can enable only what your workflow needs.

Configuration
-------------
1. Go to **Point of Sale ► Configuration ► Settings**.
2. Select your POS shop and scroll to the **Product Images** section.
3. Enable or disable images for cart lines, receipt, and invoice
   independently.
4. For the invoice toggle, save settings — the change applies to all
   Point of Sale shops because invoices are not tied to a single shop.
""",
    'author': 'Mantu Raj',
    'website': 'https://www.linkedin.com/in/mantu105/',
    'license': 'OPL-1',
    'support': 'workmantu105@gmail.com',
    'depends': [
        'account',
        'point_of_sale',
        'mail',
        'stock',
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'report/report_invoice_document.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'mr_pos_cart_receipt_product_image/static/src/overrides/models/*.js',
            'mr_pos_cart_receipt_product_image/static/src/css/pos_product_image.css',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 5.0,
    'currency': 'USD',
}
