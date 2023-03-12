# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class CostEstimation(models.Model):
    _name = 'cost.estimation'
    _description = 'Cost Estimation'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, tracking=True)
    project_id = fields.Many2one(comodel_name='project.project', required=True, tracking=True, )
    cost_estimation_lines_ids = fields.One2many(comodel_name='cost.estimation.lines', inverse_name='cost_estimation_id')

    total_estimation_lines_ids = fields.One2many(comodel_name='cost.estimation.lines',
                                                 inverse_name='total_estimation_id')

    state = fields.Selection(string="Status", selection=[
        ('draft', 'Draft'),
        ('waiting', 'Waiting to Approve'),
        ('approve', 'Approved'),
        ('revision', 'Revision'),
        ('scenario', 'Scenario'), ], default='draft', tracking=True)

    total_cost = fields.Float(string="Total Cost", compute='_compute_total_cost_estimation', store=True)
    total_demand_qty = fields.Float(string="Total Demand Quantity", compute='_compute_total_cost_estimation',
                                    store=True)
    total_done_qty = fields.Float(string="Total Done Quantity", compute='_compute_total_cost_estimation', store=True)
    total_remaining_qty = fields.Float(string="Total Remaining Quantity", compute='_compute_total_cost_estimation',
                                       store=True)
    total_estimation = fields.Float(string="Total", compute='_compute_total_cost_estimation', store=True)
    date = fields.Date()

    def get_total_actual_cost(self, line):
        result = self.env['cost.estimation.lines'].search([
            ('cost_estimation_id', '=', self._origin.id),
            ('item_estimation_id', '=', int(line['item_estimation_id'][0])),
        ])
        return sum(result.mapped('total_actual_cost'))

    def write(self, values):
        res = super(CostEstimation, self).write(values)
        if values.get('cost_estimation_lines_ids'):
            total_estimation_lines = [(5, 0, 0)]
            for rec in self:
                for line in rec.cost_estimation_lines_ids.read_group(
                        domain=[('id', 'in', rec.cost_estimation_lines_ids.ids)],
                        fields=["item_estimation_id", "sub_total"],
                        groupby=["item_estimation_id"]):
                    total_estimation_lines.append((0, 0, {
                        'item_estimation_id': line['item_estimation_id'][0],
                        'total_sub_total': line['sub_total'],
                        'total_cost': rec.get_total_actual_cost(line),
                        'is_total_estimation_line': True,
                    }))
            self.total_estimation_lines_ids = total_estimation_lines
        return res

    @api.model
    def create(self, values):
        total_estimation_lines = [(5, 0, 0)]
        for rec in self:
            for line in rec.cost_estimation_lines_ids.read_group(
                    domain=[('id', 'in', rec.cost_estimation_lines_ids.ids)],
                    fields=["item_estimation_id", "sub_total"],
                    groupby=["item_estimation_id"]):
                total_estimation_lines.append((0, 0, {
                    'item_estimation_id': line['item_estimation_id'][0],
                    'total_sub_total': line['sub_total'],
                    'total_cost': rec.get_total_actual_cost(line),
                    'is_total_estimation_line': True,
                }))
        values['total_estimation_lines_ids'] = total_estimation_lines
        return super(CostEstimation, self).create(values)

    @api.depends('cost_estimation_lines_ids')
    def _compute_total_cost_estimation(self):
        for rec in self:
            estimation_lines = rec.cost_estimation_lines_ids
            rec.total_cost = sum(estimation_lines.mapped('standard_price'))
            rec.total_demand_qty = sum(estimation_lines.mapped('demand_quantity'))
            rec.total_estimation = sum(estimation_lines.mapped('sub_total'))

    def action_waiting_approve(self):
        self.write({'state': 'waiting'})

    def action_approve(self):
        self.write({'state': 'approve'})

    def action_draft(self):
        self.write({'state': 'draft'})

    def copy(self, default=None):
        if default is None:
            default = {}
        default.update({'name': _("%s (copy)" % self.name)})
        if 'cost_estimation_lines_ids' not in default:
            print([(0, 0, line.copy_data()[0].pop('cost_estimation_id')) for line in
                   self.cost_estimation_lines_ids])
            default['cost_estimation_lines_ids'] = [(0, 0, line.copy_data()[0]) for line in
                                                    self.cost_estimation_lines_ids]
        return super(CostEstimation, self).copy(default)


class CostEstimationLines(models.Model):
    _name = 'cost.estimation.lines'
    _description = 'Cost Estimation Lines'

    cost_estimation_id = fields.Many2one(comodel_name='cost.estimation')
    project_id = fields.Many2one(comodel_name='project.project', related='cost_estimation_id.project_id', store=True)
    total_estimation_id = fields.Many2one(comodel_name='cost.estimation')
    item_estimation_id = fields.Many2one(comodel_name='item.estimation', string='Item', required=True, )
    service_id = fields.Many2one(comodel_name='product.product', string='Product/Service', required=False,
                                 domain=[('is_cost_estimation', '=', True)])
    standard_price = fields.Float(string='Cost', required=False, )
    total_cost = fields.Float()
    demand_quantity = fields.Float(required=False, )
    sub_total = fields.Float(compute='_compute_sub_total', store=True)
    total_sub_total = fields.Float('Subtotal')
    checked = fields.Boolean()
    description = fields.Char()
    is_total_estimation_line = fields.Boolean(string="", )

    @api.onchange('item_estimation_id')
    def onchange_item_estimation_id(self):
        if self.item_estimation_id:
            return {'domain': {'service_id': [
                ('is_cost_estimation', '=', True),
                ('item_ids', 'in', self.item_estimation_id.ids),
            ]}}

    @api.onchange('service_id')
    def set_standard_price(self):
        if self.service_id:
            self.standard_price = self.service_id.standard_price

    @api.depends('standard_price', 'demand_quantity')
    def _compute_sub_total(self):
        for rec in self:
            rec.sub_total = rec.standard_price * rec.demand_quantity
