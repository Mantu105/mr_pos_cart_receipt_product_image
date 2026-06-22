# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Per point-of-sale switches (related to the selected pos.config).
    pos_iface_image_orderline = fields.Boolean(
        related='pos_config_id.iface_image_orderline',
        readonly=False,
    )
    pos_iface_image_receipt = fields.Boolean(
        related='pos_config_id.iface_image_receipt',
        readonly=False,
    )

    # Global switch for the customer invoice PDF (stored as a system
    # parameter, since an invoice is not bound to a single point of sale).
    pos_image_invoice = fields.Boolean(
        string="Product Image on Invoice PDF",
        config_parameter='mr_pos_cart_receipt_product_image.image_invoice',
        help="Add a product image column to the customer invoice PDF.",
    )
