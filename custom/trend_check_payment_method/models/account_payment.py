# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountPayment(models.Model):
    _inherit = "account.payment"

    check_no = fields.Char('Check No.')
    bank_id = fields.Many2one('res.bank')
    check_date = fields.Date()

    def _prepare_move_line_default_vals(self, write_off_line_vals=None):
        res = super()._prepare_move_line_default_vals(write_off_line_vals=write_off_line_vals)
        if self.payment_method_code == 'check_printing':
            for line in res:
                line.update({'date_maturity': self.check_date, })
        return res
