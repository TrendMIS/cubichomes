# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    area = fields.Float()

    def _search_get_detail(self, website, order, options):
        search_details = super()._search_get_detail(website, order, options)
        if options.get('min_area'):
            search_details['base_domain'].append([('area', '>=', options.get('min_area'))])
        if options.get('max_area'):
            search_details['base_domain'].append([('area', '<=', options.get('max_area'))])
        return search_details
