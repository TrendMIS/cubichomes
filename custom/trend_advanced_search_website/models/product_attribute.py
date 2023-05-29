# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductAttribute(models.Model):
    _inherit = 'product.attribute'

    is_styles = fields.Boolean()
    is_bedrooms = fields.Boolean()
    is_bathrooms = fields.Boolean()
    is_floors = fields.Boolean()
    is_garage = fields.Boolean()
