from odoo import fields, models, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    
    # street = fields.Char(translate=True)
