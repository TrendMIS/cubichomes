# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    amenities_title = fields.Char('Title')
    amenities_sub_title = fields.Char('Sub Title')
    amenities_line_ids = fields.One2many(comodel_name='product.amenities', inverse_name='product_template_id')


class ProductAmenities(models.Model):
    _name = 'product.amenities'
    _description = 'Product Amenities'

    product_template_id = fields.Many2one(comodel_name='product.template')
    image = fields.Image()
    title = fields.Char()
    content = fields.Text()

