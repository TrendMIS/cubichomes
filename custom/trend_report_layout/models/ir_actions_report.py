from odoo import models


class IrActionsReport(models.AbstractModel):
    _inherit = "ir.actions.report"

    def _render_template(self, template, values=None):
        values = values or {}
        values["print_layout"] = False if "without_layout" in template else True
        return super()._render_template(template, values)
