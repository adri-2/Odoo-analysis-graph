# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_module_id = fields.Many2one('analysis.analysis', string='Custom Module')

