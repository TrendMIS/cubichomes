# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    facilities_title = fields.Char('Title')
    facilities_line_ids = fields.One2many(comodel_name='product.facilities', inverse_name='product_template_id')


class ProductFacilities(models.Model):
    _name = 'product.facilities'
    _description = 'Product Facilities'

    product_template_id = fields.Many2one(comodel_name='product.template')
    content = fields.Html()
    image = fields.Image()

