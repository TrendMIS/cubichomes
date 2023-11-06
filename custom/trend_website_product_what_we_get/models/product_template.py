# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    what_we_get_main_title = fields.Char('Main Title')
    what_we_get_sub_title = fields.Char('Sub Title')
    what_we_get_line_ids = fields.One2many(comodel_name='product.what.we.get', inverse_name='product_template_id')


class ProductWhatWeGet(models.Model):
    _name = 'product.what.we.get'
    _description = 'Product What We Get'

    product_template_id = fields.Many2one(comodel_name='product.template')
    icon = fields.Image()
    title = fields.Char()
    paragraph = fields.Char()
    attachment = fields.Binary()
    attachment_sentence = fields.Char()
