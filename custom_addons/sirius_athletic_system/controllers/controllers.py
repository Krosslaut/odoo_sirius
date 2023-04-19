# -*- coding: utf-8 -*-
# from odoo import http


# class DojoProfile(http.Controller):
#     @http.route('/dojo_profile/dojo_profile/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dojo_profile/dojo_profile/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dojo_profile.listing', {
#             'root': '/dojo_profile/dojo_profile',
#             'objects': http.request.env['dojo_profile.dojo_profile'].search([]),
#         })

#     @http.route('/dojo_profile/dojo_profile/objects/<model("dojo_profile.dojo_profile"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dojo_profile.object', {
#             'object': obj
#         })
