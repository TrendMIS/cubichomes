from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_value = fields.Monetary(string='Initial Project Value')
    final_project_value = fields.Monetary(string='Final Project Value')
    show_recompute_button = fields.Boolean(compute='_compute_show_recompute_button')
    lock_final = fields.Boolean(default=False)
    eligible_order = fields.Boolean(default=False)

    @api.depends('project_value', 'final_project_value')
    def _compute_show_recompute_button(self):
        for rec in self:
            rec.show_recompute_button = False if rec.final_project_value <= rec.project_value else True

    def action_recompute_value(self):
        lst = []
        is_eligible = self.order_line.filtered(lambda l: l.is_eligible)
        if not is_eligible:
            raise ValidationError('There is no Eligible Line for change')

        for line in self.order_line.filtered(lambda l: l.is_eligible):
            new_unit_price = self.project_value * (line.percentage / 100)
            line_data = line.copy_data({
                'name': 'variants for project value change',
                'price_unit': new_unit_price - line.price_unit,
                'is_eligible': False
            })
            lst.append((0, 0, line_data[0]))
        order_data = self.copy_data({
            'origin': self.name,
            'date_order': datetime.now(),
            'eligible_order': True,
            'order_line': lst

        })
        self.env['sale.order'].create(order_data)
        self.write({'lock_final': True})


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
