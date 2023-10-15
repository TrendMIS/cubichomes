# -*- coding: utf-8 -*-

from odoo import models, fields


class Company(models.Model):
    _inherit = 'res.company'

    arabic_name = fields.Char(related='partner_id.arabic_name')
