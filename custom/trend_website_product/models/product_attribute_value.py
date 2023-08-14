# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'

    layout_icon = fields.Image()
