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


class AnalysisDataGenerator(models.TransientModel):
    _name = 'analysis.data.generator'
    _description = 'Generate Dummy Data for Order Analysis'

    @api.model
    def generate_data(self):
        # Define time periods and weekdays
        time_periods = ['0', '1', '2', '3']
        weekdays = ['0', '1', '2', '3', '4', '5', '6']

        # Start date for the data generation
        start_date = datetime.strptime('2024-07-20', '%Y-%m-%d')

        # Generate data for 365 days
        for i in range(365):
            current_date = start_date + timedelta(days=i)
            weekday = current_date.weekday()  # 0 is Monday, 6 is Sunday

            for time_period in time_periods:
                self.env['analysis.analysis'].create({
                    'date': current_date.date(),
                    'weekday': str(weekday),
                    'time_period': time_period,
                    'order_count': random.randint(0, 50)  # Random number of orders between 0 and 50
                })