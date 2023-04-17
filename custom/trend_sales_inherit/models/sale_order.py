from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_value = fields.Monetary(
        string='Project Value',
        required=False)

    def action_recompute_value(self):
        for line in self.order_line.filtered(lambda l: l.is_eligible):
            new_unit_price = self.project_value * (line.percentage / 100)
            if new_unit_price > line.price_unit:
                data = line.copy_data({
                    'name': 'variants for project value change',
                    'order_id': self.id,
                    'price_unit': new_unit_price - line.price_unit,
                    'is_eligible': False
                })
                self.env['sale.order.line'].sudo().create(data)


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
            if not line.order_id.state == 'sale':
                line.price_unit = line.order_id.project_value * (line.percentage / 100)
