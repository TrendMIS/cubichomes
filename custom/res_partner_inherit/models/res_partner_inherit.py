from odoo import fields, models, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    
    street = fields.Char(translate=True)
    street2 = fields.Char(translate=True)
    city = fields.Char(translate=True)


class ResCompanyInherit(models.Model):
    _inherit = 'res.company'

    street = fields.Char(translate=True)
    street2 = fields.Char(translate=True)
    city = fields.Char(translate=True)