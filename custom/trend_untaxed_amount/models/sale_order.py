# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    untaxed_amount = fields.Float(compute='_compute_untaxed_amount', store=True)

    @api.depends('price_subtotal', 'price_tax')
    def _compute_untaxed_amount(self):
        for rec in self:
            rec.untaxed_amount = rec.price_subtotal - rec.price_tax
