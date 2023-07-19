# -*- coding: utf-8 -*-

from odoo import models, fields


class LayoutPlan(models.Model):
    _name = 'layout.plan'
    _description = 'Layout Plan'

    name = fields.Char()

