# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    interior_design_line_ids = fields.One2many(comodel_name='product.interior.design',
                                               inverse_name='product_template_id')


class ProductInteriorDesign(models.Model):
    _name = 'product.interior.design'
    _description = 'Product Interior Design'

    product_template_id = fields.Many2one(comodel_name='product.template')
    image_count = fields.Selection(selection=[('image_1', '1'), ('image_2', '2'), ],
                                   default='image_1', required=True)
    is_decoration = fields.Boolean('Decorations')
    image_1 = fields.Image()
    image_2 = fields.Image()
    title = fields.Char()
    content = fields.Text()
