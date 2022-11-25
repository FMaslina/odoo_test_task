# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo-fmaslina(http.Controller):
#     @http.route('/odoo-fmaslina/odoo-fmaslina', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-fmaslina/odoo-fmaslina/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-fmaslina.listing', {
#             'root': '/odoo-fmaslina/odoo-fmaslina',
#             'objects': http.request.env['odoo-fmaslina.odoo-fmaslina'].search([]),
#         })

#     @http.route('/odoo-fmaslina/odoo-fmaslina/objects/<model("odoo-fmaslina.odoo-fmaslina"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-fmaslina.object', {
#             'object': obj
#         })
