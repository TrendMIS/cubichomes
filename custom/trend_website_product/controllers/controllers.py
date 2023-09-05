# -*- coding: utf-8 -*-
# from odoo import http


# class TrendWebsiteProduct(http.Controller):
#     @http.route('/trend_website_product/trend_website_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trend_website_product/trend_website_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trend_website_product.listing', {
#             'root': '/trend_website_product/trend_website_product',
#             'objects': http.request.env['trend_website_product.trend_website_product'].search([]),
#         })

#     @http.route('/trend_website_product/trend_website_product/objects/<model("trend_website_product.trend_website_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trend_website_product.object', {
#             'object': obj
#         })
