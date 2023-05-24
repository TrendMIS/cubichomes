# -*- coding: utf-8 -*-
# from odoo import http


# class TrendWebsiteProductCard(http.Controller):
#     @http.route('/trend_website_product_card/trend_website_product_card', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trend_website_product_card/trend_website_product_card/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trend_website_product_card.listing', {
#             'root': '/trend_website_product_card/trend_website_product_card',
#             'objects': http.request.env['trend_website_product_card.trend_website_product_card'].search([]),
#         })

#     @http.route('/trend_website_product_card/trend_website_product_card/objects/<model("trend_website_product_card.trend_website_product_card"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trend_website_product_card.object', {
#             'object': obj
#         })
