from odoo import fields, models, api
from num2words import num2words


class AccountMove(models.Model):
    _inherit = 'account.move'

    sale_order_id = fields.Many2one(comodel_name='sale.order', string='Sale Order', required=False)
    project_id = fields.Many2one(comodel_name='project.project', string='Project')
    amount_total_words = fields.Char(compute="_get_words")
    amount_total_words_english = fields.Char(compute="_get_words")
    lang = fields.Selection(related='partner_id.lang', string='Language', readonly=False,
                            help="All the emails and documents sent to this contact will be translated in this language.")

    @api.onchange('sale_order_id')
    def _set_project(self):
        if self.sale_order_id.project_id:
            self.project_id = self.sale_order_id.project_id.id
        else:
            self.project_id = False

    @api.depends("amount_total")
    def _get_words(self):
        for record in self:
            record.amount_total_words = num2words(record.amount_total, lang="ar")
            record.amount_total_words_english = num2words(record.amount_total, lang="en")

    @api.model
    def default_get(self, field):
        res = super(AccountMove, self).default_get(field)
        active_model = self.env.context.get('active_model')
        if active_model == 'sale.order' and len(self.env.context.get('active_ids', [])) <= 1:
            sale_order = self.env[active_model].browse(self.env.context.get('active_id')).exists()
            if sale_order:
                res.update(
                    sale_order_id=sale_order.id,
                )

        return res


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

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
