# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    iface_image_orderline = fields.Boolean(
        string="Product Image on Order Lines",
        help="Show the product image on each line of the Point of Sale cart.",
    )
    iface_image_receipt = fields.Boolean(
        string="Product Image on Receipt",
        help="Print the product image next to each line on the customer "
             "receipt.",
    )

    @api.model
    def _load_pos_data_fields(self, config_id):
        """Make sure the new fields are sent to the POS frontend.

        The base ``pos.config`` implementation returns an empty list, which
        makes ``search_read`` load *all* fields, so our fields are already
        available. We only append them when a customization restricts the
        loaded fields to an explicit list, to stay compatible in both cases.
        """
        result = super()._load_pos_data_fields(config_id)
        if result:
            result += ['iface_image_orderline', 'iface_image_receipt']
        return result
