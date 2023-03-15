from odoo import api, fields, models


class ProjectMilestone(models.Model):
    _inherit = 'project.milestone'

    approval_cost = fields.Float(compute='_compute_approval_cost')

    def _compute_approval_cost(self):
        for rec in self:
            tasks = self.env['project.task'].search([('milestone_id', '=', rec.id)])
            rec.approval_cost = sum(tasks.mapped('approval_cost'))
