# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    first_inspiration_title = fields.Char('Title')
    second_inspiration_title = fields.Char('Title')
    second_inspiration_content = fields.Html('Content')
    second_inspiration_image = fields.Image('Image')
    first_inspiration_ids = fields.One2many(comodel_name='first.product.inspiration',
                                            inverse_name='product_template_id')
    second_inspiration_ids = fields.One2many(comodel_name='second.product.inspiration',
                                             inverse_name='product_template_id')


class FirstProductInspiration(models.Model):
    _name = 'first.product.inspiration'
    _description = 'First Product Inspiration'

    product_template_id = fields.Many2one(comodel_name='product.template')
    content = fields.Html()
    image = fields.Image()


class SecondProductInspiration(models.Model):
    _name = 'second.product.inspiration'
    _description = 'Second Product Inspiration'

    product_template_id = fields.Many2one(comodel_name='product.template')
    content = fields.Html()
    image = fields.Image()
