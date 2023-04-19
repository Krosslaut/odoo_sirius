# -*- coding: utf-8 -*-
# from odoo import http


# class SiriusAthleticCore(http.Controller):
#     @http.route('/sirius_athletic_core/sirius_athletic_core/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sirius_athletic_core/sirius_athletic_core/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sirius_athletic_core.listing', {
#             'root': '/sirius_athletic_core/sirius_athletic_core',
#             'objects': http.request.env['sirius_athletic_core.sirius_athletic_core'].search([]),
#         })

#     @http.route('/sirius_athletic_core/sirius_athletic_core/objects/<model("sirius_athletic_core.sirius_athletic_core"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sirius_athletic_core.object', {
#             'object': obj
#         })
