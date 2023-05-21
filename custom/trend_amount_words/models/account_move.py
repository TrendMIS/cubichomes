# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    lang = fields.Selection(related='partner_id.lang', string='Language', readonly=False, reaquired=True)
