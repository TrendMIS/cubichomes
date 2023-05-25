# -*- coding: utf-8 -*-
from odoo.addons.website.controllers.main import Website
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http


class AdvancedSearch(Website):

    def _get_product_attribute(self):
        product_attribute = http.request.env['product.attribute'].search([])
        bedrooms = product_attribute.filtered(lambda p: p.is_bedrooms).value_ids
        bathrooms = product_attribute.filtered(lambda p: p.is_bathrooms).value_ids
        floors = product_attribute.filtered(lambda p: p.is_floors).value_ids
        styles = product_attribute.filtered(lambda p: p.is_styles).value_ids
        return {
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'floors': floors,
            'styles': styles,
        }

    @http.route('/', type='http', auth="public", website=True, sitemap=True)
    def index(self, **kw):
        super().index(**kw)
        values = {}
        product_attribute = self._get_product_attribute()
        if product_attribute:
            values.update(product_attribute)
        values['min_area'] = 10
        values['max_area'] = 10000
        return http.request.render("website.homepage", values)


class AdvancedSearchDomain(WebsiteSale):

    def _get_search_options(self, **post):
        options = super()._get_search_options(**post)
        product_attribute = http.request.env['product.attribute.value']
        lst = []
        if post.get('bedroom_id'):
            value = product_attribute.browse(int(post.get('bedroom_id')))
            lst.append([value.attribute_id.id, value.id])
        if post.get('bathroom_id'):
            value = product_attribute.browse(int(post.get('bathroom_id')))
            lst.append([value.attribute_id.id, value.id])
        if post.get('floor_id'):
            value = product_attribute.browse(int(post.get('floor_id')))
            lst.append([value.attribute_id.id, value.id])
        if post.get('style'):
            value = product_attribute.browse(int(post.get('style')))
            lst.append([value.attribute_id.id, value.id])
        if lst:
            options.update({
                'attrib_values': lst,
            })
        if post.get('min_area'):
            min_area = post.get('min_area').replace(",", "")
            options.update({
                'min_area': float(min_area),
            })
        if post.get('max_area'):
            max_area = post.get('max_area').replace(",", "")
            options.update({
                'max_area': float(max_area),
            })
        return options
