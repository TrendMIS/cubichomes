# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    products_ids = fields.Many2many('product.product', compute='_compute_products_ids', store=True)

    @api.depends('invoice_line_ids', 'invoice_line_ids.product_id')
    def _compute_products_ids(self):
        for move in self:
            move.products_ids = move.invoice_line_ids.mapped('product_id')
