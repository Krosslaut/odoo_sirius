# -*- coding: utf-8 -*-
# from odoo import http


# class SiriusMmedicalAddon(http.Controller):
#     @http.route('/sirius_mmedical_addon/sirius_mmedical_addon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sirius_mmedical_addon/sirius_mmedical_addon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sirius_mmedical_addon.listing', {
#             'root': '/sirius_mmedical_addon/sirius_mmedical_addon',
#             'objects': http.request.env['sirius_mmedical_addon.sirius_mmedical_addon'].search([]),
#         })

#     @http.route('/sirius_mmedical_addon/sirius_mmedical_addon/objects/<model("sirius_mmedical_addon.sirius_mmedical_addon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sirius_mmedical_addon.object', {
#             'object': obj
#         })
