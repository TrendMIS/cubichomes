# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    kitchen_title = fields.Char('Title')
    kitchen_image = fields.Image('Image')
    kitchen_content = fields.Html('Content')
