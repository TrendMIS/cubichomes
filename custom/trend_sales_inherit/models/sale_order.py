from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_value = fields.Monetary(
        string='Project Value',
        required=False)
    
    
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_eligible = fields.Boolean(
        string='Eligible for change',
        required=False)

    percentage = fields.Float(
        string='Percentage',
        required=False)
    





