# -*- coding: utf-8 -*-
# from odoo import http


# class SiriusAthleticCategory(http.Controller):
#     @http.route('/sirius_athletic_category/sirius_athletic_category/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sirius_athletic_category/sirius_athletic_category/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sirius_athletic_category.listing', {
#             'root': '/sirius_athletic_category/sirius_athletic_category',
#             'objects': http.request.env['sirius_athletic_category.sirius_athletic_category'].search([]),
#         })

#     @http.route('/sirius_athletic_category/sirius_athletic_category/objects/<model("sirius_athletic_category.sirius_athletic_category"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sirius_athletic_category.object', {
#             'object': obj
#         })
