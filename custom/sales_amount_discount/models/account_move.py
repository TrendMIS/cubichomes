from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    sale_order_id = fields.Many2one(comodel_name='sale.order', string='Sale Order', required=False)
    project_id = fields.Many2one(comodel_name='project.project', string='Project')
    is_percentage = fields.Boolean(
        string='Is_percentage',
        compute='_compute_is_percentage',
        required=False)

    # @api.model
    # def _get_view(self, view_id=None, view_type='form', **options):
    #     arch, view = super()._get_view(view_id, view_type, **options)
    #     for node in arch.xpath("//field[@name='invoice_line_ids']/tree/field[@name='quantity']"):
    #         if self.is_percentage:
    #             node.set = ('string', 'Percentage')
    #         else:
    #             node.set = ('string', 'Quantity')
    #
    #     return arch, view

    @api.depends('invoice_line_ids')
    def _compute_is_percentage(self):
        for rec in self:
            if rec.invoice_line_ids:
                if rec.invoice_line_ids[0].quantity >= 1:
                    rec.is_percentage = False
                else:
                    rec.is_percentage = True
            else:
                rec.is_percentage = False

    @api.onchange('sale_order_id')
    def _set_project(self):
        if self.sale_order_id.project_id:
            self.project_id = self.sale_order_id.project_id.id
        else:
            self.project_id = False

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
    is_percentage = fields.Boolean(
        string='Is_percentage',
        related='move_id.is_percentage',
        required=False)

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
