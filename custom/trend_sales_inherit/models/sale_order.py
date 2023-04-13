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

    @api.depends('product_id', 'product_uom', 'product_uom_qty', 'percentage', 'order_id.project_value')
    def _compute_price_unit(self):
        for line in self:
            line.price_unit = line.order_id.project_value * (line.percentage / 100)


    





