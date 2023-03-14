from odoo import fields, models, api
from num2words import num2words


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    amount_total_words = fields.Char(compute="_get_words")
    amount_total_words_english = fields.Char(compute="_get_words")

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


    @api.depends("amount_total")
    def _get_words(self):
        for record in self:
            record.amount_total_words = num2words(record.amount_total, lang="ar")
            record.amount_total_words_english = num2words(record.amount_total, lang="en")


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

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            tax_results = self.env['account.tax']._compute_taxes([line._convert_to_tax_base_line_dict()])
            totals = list(tax_results['totals'].values())[0]
            amount_untaxed = totals['amount_untaxed']
            amount_tax = totals['amount_tax']

            line.update({
                'price_subtotal': amount_untaxed + amount_tax,
                'price_tax': amount_tax,
                'price_total': amount_untaxed + amount_tax,
            })
            if self.env.context.get('import_file', False) and not self.env.user.user_has_groups(
                    'account.group_account_manager'):
                line.tax_id.invalidate_recordset(['invoice_repartition_line_ids'])

