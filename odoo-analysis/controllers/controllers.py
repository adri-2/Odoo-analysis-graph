# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo13-custom-addons/odoo-analysis(http.Controller):
#     @http.route('/odoo13-custom-addons/odoo-analysis/odoo13-custom-addons/odoo-analysis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo13-custom-addons/odoo-analysis/odoo13-custom-addons/odoo-analysis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo13-custom-addons/odoo-analysis.listing', {
#             'root': '/odoo13-custom-addons/odoo-analysis/odoo13-custom-addons/odoo-analysis',
#             'objects': http.request.env['odoo13-custom-addons/odoo-analysis.odoo13-custom-addons/odoo-analysis'].search([]),
#         })

#     @http.route('/odoo13-custom-addons/odoo-analysis/odoo13-custom-addons/odoo-analysis/objects/<model("odoo13-custom-addons/odoo-analysis.odoo13-custom-addons/odoo-analysis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo13-custom-addons/odoo-analysis.object', {
#             'object': obj
#         })
