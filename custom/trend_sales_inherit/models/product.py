from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import datetime


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    internal_service_type = fields.Selection([
        ("design", "Design"),
        ("supervision", "Supervision"),
    ])
