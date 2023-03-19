from odoo import api, fields, models


class ProjectMilestone(models.Model):
    _inherit = 'project.milestone'

    approval_cost = fields.Float(compute='_compute_approval_cost')

    def _compute_approval_cost(self):
        for rec in self:
            tasks = self.env['project.task'].search([('milestone_id', '=', rec.id)])
            rec.approval_cost = sum(tasks.mapped('approval_cost'))

    def action_view_document(self):
        action = self.env['ir.actions.act_window']._for_xml_id('documents.document_action')
        domain = [('res_model', '=', 'project.task'), ('res_id', 'in', self.task_ids.ids)]
        action['domain'] = domain
        return action
