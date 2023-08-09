# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    layout_plan_ids = fields.Many2many('layout.plan')
    product_gallery_ids = fields.One2many(comodel_name='product.gallery.image', inverse_name='product_template_id')
    area_table_image = fields.Image()
    first_plan_image = fields.Image()
    second_plan_image = fields.Image()


class ProductGalleryImage(models.Model):
    _name = 'product.gallery.image'
    _description = 'Product Gallery Image'

    product_template_id = fields.Many2one(comodel_name='product.template')
    name = fields.Char()
    image = fields.Image()
