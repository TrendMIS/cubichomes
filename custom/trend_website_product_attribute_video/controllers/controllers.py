# -*- coding: utf-8 -*-
# from odoo import http


# class TrendWebsiteProductAttributeVidoe(http.Controller):
#     @http.route('/trend_website_product_attribute_vidoe/trend_website_product_attribute_vidoe', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trend_website_product_attribute_vidoe/trend_website_product_attribute_vidoe/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trend_website_product_attribute_vidoe.listing', {
#             'root': '/trend_website_product_attribute_vidoe/trend_website_product_attribute_vidoe',
#             'objects': http.request.env['trend_website_product_attribute_vidoe.trend_website_product_attribute_vidoe'].search([]),
#         })

#     @http.route('/trend_website_product_attribute_vidoe/trend_website_product_attribute_vidoe/objects/<model("trend_website_product_attribute_vidoe.trend_website_product_attribute_vidoe"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trend_website_product_attribute_vidoe.object', {
#             'object': obj
#         })
