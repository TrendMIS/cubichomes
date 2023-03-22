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
