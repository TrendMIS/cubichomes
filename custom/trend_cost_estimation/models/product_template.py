from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_cost_estimation = fields.Boolean(string="Cost Estimation", )
    item_ids = fields.Many2many(comodel_name="item.estimation", string="Items", )
