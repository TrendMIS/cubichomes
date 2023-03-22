from odoo import fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    project_id = fields.Many2one('project.project')
    analytic_account_id = fields.Many2one(related='project_id.analytic_account_id', store=True)

    def action_post(self):
        super().action_post()
        self.move_id.project_id = self.project_id.id
