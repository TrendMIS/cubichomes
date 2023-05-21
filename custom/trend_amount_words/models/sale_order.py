# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    lang = fields.Selection(related='partner_id.lang', string='Language', readonly=False, reaquired=True)
