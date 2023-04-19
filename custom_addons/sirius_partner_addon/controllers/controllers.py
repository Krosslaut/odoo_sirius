# -*- coding: utf-8 -*-
# from odoo import http


# class SiriusPartnerAddon(http.Controller):
#     @http.route('/sirius_partner_addon/sirius_partner_addon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sirius_partner_addon/sirius_partner_addon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sirius_partner_addon.listing', {
#             'root': '/sirius_partner_addon/sirius_partner_addon',
#             'objects': http.request.env['sirius_partner_addon.sirius_partner_addon'].search([]),
#         })

#     @http.route('/sirius_partner_addon/sirius_partner_addon/objects/<model("sirius_partner_addon.sirius_partner_addon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sirius_partner_addon.object', {
#             'object': obj
#         })
