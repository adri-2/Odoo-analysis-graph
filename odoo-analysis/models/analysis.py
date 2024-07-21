# -*- coding: utf-8 -*-
from random import random

from odoo import models, fields, api
from datetime import datetime, timedelta

class OrderAnalysis(models.Model):
    _name = 'analysis.analysis'
    _description = 'Order Analysis'

    date = fields.Date('Date')
    weekday = fields.Selection(
        [('0', 'Lundi'), ('1', 'Mardi'), ('2', 'Mercredi'), ('3', 'Jeudi'), ('4', 'Vendredi'), ('5', 'Samedi'), ('6', 'Dimanche')],
        string='Jours de la semaine')
    time_period = fields.Selection(
        [('0', '06:00-10:00'), ('1', '10:00-14:00'), ('2', '14:00-18:00'), ('3', '18:00-22:00')],
        string='Période de temps')
    order_count = fields.Integer('Nombre de commandes')
    #order_count = fields.Integer('Nombre de commandes', compute='_compute_order_count', store=True)
    sale_order_ids = fields.One2many('sale.order', 'custom_module_id', string='Sale Orders')

