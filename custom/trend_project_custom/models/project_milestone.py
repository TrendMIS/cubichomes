from odoo import api, fields, models


class ProjectMilestone(models.Model):
    _inherit = 'project.milestone'

    approval_cost = fields.Float()
