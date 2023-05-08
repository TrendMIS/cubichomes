from odoo import fields, models, api
from num2words import num2words


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_id = fields.Many2one(
        comodel_name='project.project',
        compute='_compute_project_id',
        string='Project',
        required=False)

    def _compute_project_id(self):
        for rec in self:
            project = rec.env['project.project'].search([('sale_order_id', '=', rec.id)])
            if project:
                rec.project_id = project.id
            else:
                rec.project_id = False


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Float(compute='_get_discount_amount', store=True, digits=(15, 2), readonly=False)
    full_discount = fields.Float(compute='_set_discount_amount', store=True, digits=(15, 2), readonly=False)
    discount = fields.Float(digits=(15, 20))

    @api.depends('full_discount')
    def _get_discount_amount(self):
        for rec in self:
            if rec.full_discount:
                rec.discount_amount = rec.full_discount / 100 * rec.price_unit
                rec.discount = rec.full_discount
            else:
                rec.discount_amount = 0.0
                rec.discount = 0.0

    @api.depends('discount_amount')
    def _set_discount_amount(self):
        for rec in self:
            if rec.discount_amount:
                rec.discount = (rec.discount_amount / rec.price_unit) * 100
                rec.full_discount = (rec.discount_amount / rec.price_unit) * 100
            else:
                rec.discount = 0.0
                rec.full_discount = 0.0
