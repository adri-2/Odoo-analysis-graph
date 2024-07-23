"""
from odoo import models, fields, api
from datetime import datetime

class OrderAnalysis(models.Model):
    _name = 'analysis.analysis'
    _description = 'Analyse des Commandes'

    date = fields.Date('Date')
    weekday = fields.Selection(
        [('0', 'Lundi'), ('1', 'Mardi'), ('2', 'Mercredi'), ('3', 'Jeudi'), ('4', 'Vendredi'), ('5', 'Samedi'),
         ('6', 'Dimanche')],
        string='Jour de la Semaine')
    time_period = fields.Selection(
        [('0', '01:00-04:00'), ('1', '04:00-08:00'), ('2', '08:00-12:00'), ('3', '12:00-16:00'), ('4', '16:00-20:00'),
         ('5', '20:00-00:00'),('6', '20:00-00:00')],
        string='Période de Temps')
    order_count = fields.Integer('Nombre de Commandes')
    sale_order_ids = fields.One2many('sale.order', 'custom_module_id', string='Commandes')

    @api.model
    def analyze_orders(self):
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

        orders = self.env['sale.order'].search([])
        analysis_data = {}

        for order in orders:
            order_date = order.create_date
            date_str = order_date.strftime('%Y-%m-%d')
            weekday = str(order_date.weekday())
            hour = order_date.hour

            if 1 <= hour < 4:
                period = '0'
            elif 4 <= hour < 8:
                period = '1'
            elif 8 <= hour < 12:
                period = '2'
            elif 12 <= hour < 16:
                period = '3'
            elif 16 <= hour < 20:
                period = '4'
            elif 20 <= hour < 24:
                period = '5'
            else:
                continue

            key = (date_str, weekday, period)

            if key not in analysis_data:
                analysis_data[key] = {
                    'date': date_str,
                    'weekday': weekday,
                    'time_period': period,
                    'order_count': 0,
                    'sale_order_ids': []
                }

            analysis_data[key]['order_count'] += 1
            analysis_data[key]['sale_order_ids'].append(order.id)

        for key, data in analysis_data.items():
            self.create({
                'date': data['date'],
                'weekday': data['weekday'],
                'time_period': data['time_period'],
                'order_count': data['order_count'],
                'sale_order_ids': [(6, 0, data['sale_order_ids'])]
            })
        print("=================================================")

    def button_analyze_orders(self):
        self.analyze_orders()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
"""
from odoo import models, fields, api
from datetime import datetime

class OrderAnalysis(models.Model):
    _name = 'analysis.analysis'
    _description = 'Analyse des Commandes'

    date = fields.Date('Date')
    weekday = fields.Selection(
        [('0', 'Lundi'), ('1', 'Mardi'), ('2', 'Mercredi'), ('3', 'Jeudi'), ('4', 'Vendredi'), ('5', 'Samedi'),
         ('6', 'Dimanche')],
        string='Jour de la Semaine')
    time_period = fields.Selection(
        [('0', '01:00-04:00'), ('1', '04:00-08:00'), ('2', '08:00-12:00'), ('3', '12:00-16:00'), ('4', '16:00-20:00'),
         ('5', '20:00-00:00'), ('6', '20:00-00:00')],
        string='Période de Temps')
    order_count = fields.Integer('Nombre de Commandes')
    sale_order_ids = fields.One2many('sale.order', 'custom_module_id', string='Commandes')

    @api.model
    def analyze_orders(self):
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

        orders = self.env['sale.order'].search([])
        analysis_data = {}

        # Récupérer tous les IDs de commandes déjà analysées
        analyzed_order_ids = self.env['analysis.analysis'].search([]).mapped('sale_order_ids').ids

        for order in orders:
            if order.id in analyzed_order_ids:
                continue  # Skip already analyzed orders

            order_date = order.create_date
            date_str = order_date.strftime('%Y-%m-%d')
            weekday = str(order_date.weekday())
            hour = order_date.hour

            if 1 <= hour < 4:
                period = '0'
            elif 4 <= hour < 8:
                period = '1'
            elif 8 <= hour < 12:
                period = '2'
            elif 12 <= hour < 16:
                period = '3'
            elif 16 <= hour < 20:
                period = '4'
            elif 20 <= hour < 24:
                period = '5'
            else:
                continue

            key = (date_str, weekday, period)

            if key not in analysis_data:
                analysis_data[key] = {
                    'date': date_str,
                    'weekday': weekday,
                    'time_period': period,
                    'order_count': 0,
                    'sale_order_ids': []
                }

            analysis_data[key]['order_count'] += 1
            analysis_data[key]['sale_order_ids'].append(order.id)

        for key, data in analysis_data.items():
            self.create({
                'date': data['date'],
                'weekday': data['weekday'],
                'time_period': data['time_period'],
                'order_count': data['order_count'],
                'sale_order_ids': [(6, 0, data['sale_order_ids'])]
            })
        print("=================================================")
