# -*- coding: utf-8 -*-

from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    arabic_name = fields.Char()


class Company(models.Model):
    _inherit = 'res.company'

    arabic_name = fields.Char()
