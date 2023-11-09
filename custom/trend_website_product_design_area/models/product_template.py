# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    design_area_title = fields.Text('Title')
    design_area_content = fields.Text('Content')
