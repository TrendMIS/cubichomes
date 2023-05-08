from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_value = fields.Monetary(string='Initial Project Value')
    supervision_percentage = fields.Float()
    supervision_amount = fields.Monetary()
    design_percentage = fields.Float()
    design_amount = fields.Monetary()
    final_project_value = fields.Monetary(string='Corrected Project Value')
    show_recompute_button = fields.Boolean(compute='_compute_show_recompute_button')
    lock_final = fields.Boolean(default=False)
    eligible_order = fields.Boolean(default=False)
    sale_id = fields.Many2one('sale.order')

    @api.depends('project_value', 'final_project_value')
    def _compute_show_recompute_button(self):
        for rec in self:
            rec.show_recompute_button = False if rec.final_project_value <= rec.project_value else True

    def action_recompute_value(self):
        eligible_lines = self.order_line.filtered(lambda l: l.is_eligible)
        if not eligible_lines:
            raise ValidationError('There is no Eligible Line for change')
        new_design_lines = self._generate_new_lines(eligible_lines, "design", self.design_percentage)
        new_supervision_lines = self._generate_new_lines(eligible_lines, "supervision", self.supervision_percentage)
        order_data = self.copy_data({
            'origin': self.name,
            'sale_id': self.id,
            'date_order': datetime.now(),
            'eligible_order': True,
            'order_line': new_design_lines + new_supervision_lines
        })
        sale_order = self.env['sale.order'].create(order_data)
        self.write({'lock_final': True})
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'res_id': sale_order.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
        }

    def _generate_new_lines(self, eligible_lines, internal_service_type, service_type_percentage):
        new_lines = []
        lines = eligible_lines.filtered(lambda l: l.internal_service_type == internal_service_type)
        for line in lines:
            difference_amount = (self.final_project_value - self.project_value) * (service_type_percentage / 100)
            amount = difference_amount * (line.percentage / 100)
            new_line_data = line.copy_data({
                'name': f'variants for project value change [{internal_service_type}]',
                'price_unit': amount,
                'is_eligible': False
            })
            new_lines.append((0, 0, new_line_data[0]))
        return new_lines

    def get_related_sale(self):
        return {
            'name': 'Related Orders/Quotations',
            'view_type': 'form',
            'domain': [('id', '=', self.sale_id.id)],
            'view_mode': 'tree,form',
            'res_model': 'sale.order',
            'type': 'ir.actions.act_window',
        }

    @api.onchange("project_value")
    def _onchange_project_value(self):
        self._onchange_supervision_percentage()
        self._onchange_design_percentage()

    @api.onchange("supervision_percentage")
    def _onchange_supervision_percentage(self):
        self.supervision_amount = self.project_value * self.supervision_percentage / 100

    @api.onchange("supervision_amount")
    def _onchange_supervision_amount(self):
        if self.project_value:
            percentage = self.supervision_amount * 100 / self.project_value
            self.supervision_percentage = round(percentage, 2)

    @api.onchange("design_percentage")
    def _onchange_design_percentage(self):
        self.design_amount = self.project_value * self.design_percentage / 100

    @api.onchange("design_amount")
    def _onchange_design_amount(self):
        if self.project_value:
            percentage = self.design_amount * 100 / self.project_value
            self.design_percentage = round(percentage, 2)

    @api.constrains("design_amount", "percentage_amount", "order_line")
    def validate_total_service_amount(self):
        for rec in self:
            design_lines = rec.order_line.filtered(lambda l: l.internal_service_type == "design")
            if sum(design_lines.mapped("price_total")) > rec.design_amount:
                raise ValidationError("Design lines total price exceeds the total design amount")
            supervision_lines = rec.order_line.filtered(lambda l: l.internal_service_type == "supervision")
            if sum(supervision_lines.mapped("price_total")) > rec.supervision_amount:
                raise ValidationError("Supervision lines total price exceeds the total supervision amount")


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_eligible = fields.Boolean(
        string='Eligible for change',
        required=False)

    percentage = fields.Float(
        string='Percentage',
        required=False)

    internal_service_type = fields.Selection(related="product_template_id.internal_service_type")

    @api.onchange('percentage',
                  "internal_service_type",
                  'order_id.supervision_amount',
                  'order_id.design_amount')
    def _compute_price_unit(self):
        if not self.internal_service_type or self.order_id.state == 'sale':
            return
        amount = self._get_service_type_amount()
        self.price_unit = amount * (self.percentage / 100)

    @api.onchange('price_unit',
                  "internal_service_type",
                  'order_id.supervision_amount',
                  'order_id.design_amount')
    def _compute_percentage(self):
        if not self.internal_service_type or self.order_id.state == 'sale':
            return
        amount = self._get_service_type_amount()
        if amount:
            self.percentage = (self.price_unit / amount) * 100

    def _get_service_type_amount(self):
        if self.internal_service_type == "design":
            return self.order_id.design_amount
        return self.order_id.supervision_amount
