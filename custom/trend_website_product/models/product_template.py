# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    layout_plan_ids = fields.Many2many('layout.plan')
