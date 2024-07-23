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
        [('0', '06:00-10:00'), ('1', '10:00-14:00'), ('2', '14:00-18:00'), ('3', '18:00-22:00')],
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

            if 6 <= hour < 10:
                period = '0'
            elif 10 <= hour < 14:
                period = '1'
            elif 14 <= hour < 18:
                period = '2'
            elif 18 <= hour < 22:
                period = '3'
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
