from odoo import fields, models, api


class AccountTax(models.Model):
    _inherit = 'account.tax'

    name = fields.Char(translate=True)