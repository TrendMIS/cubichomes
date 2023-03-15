from odoo import api, fields, models


class Task(models.Model):
    _inherit = 'project.task'

    approval_cost = fields.Float()
