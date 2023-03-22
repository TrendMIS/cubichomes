from odoo import api, fields, models


class Task(models.Model):
    _inherit = 'project.task'

    approval_cost = fields.Float()
    paid_by_us = fields.Boolean()
    move_line_ids = fields.Many2many("account.move.line")

    @api.onchange("paid_by_us")
    def onchange_paid_by_us(self):
        if not self.paid_by_us:
            self.move_line_ids = False
            return
        ids = self._calc_move_line_ids_domain()
        return {
            "domain": {"move_line_ids": [("id", "in", ids)]}
        }

    def _calc_move_line_ids_domain(self):
        cash_bank_move_lines = self.env["account.move.line"].search([
            ("account_id.account_type", "=", "asset_cash"),
            ("move_id.state", "=", "posted"),
            ("move_id.project_id", "=", self.project_id.id)
        ])
        return cash_bank_move_lines.ids

