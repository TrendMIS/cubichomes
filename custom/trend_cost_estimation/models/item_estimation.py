# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ItemEstimation(models.Model):
    _name = 'item.estimation'
    _description = 'Item Estimation'

    name = fields.Char(required=True)
    cost_depend_on = fields.Selection(string="Costing depends on", selection=[
        ('qty', 'Quantity'), ('amount', 'Amount'), ], default='qty', required=True)
