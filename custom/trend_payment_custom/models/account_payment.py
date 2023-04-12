# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    journal_items_ids = fields.One2many(comodel_name='account.move.line', inverse_name='payment_id')
