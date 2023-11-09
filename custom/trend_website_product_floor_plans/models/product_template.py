# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    floor_plans_title = fields.Char('Title')
    floor_plans_sub_title = fields.Char('Sub Title')
    floor_plans_line_ids = fields.One2many(comodel_name='product.floor.plans', inverse_name='product_template_id')


class ProductFloorPlans(models.Model):
    _name = 'product.floor.plans'
    _description = 'Product Floor Plans'

    product_template_id = fields.Many2one(comodel_name='product.template')
    title = fields.Char()
    content = fields.Html()
    image = fields.Image()

