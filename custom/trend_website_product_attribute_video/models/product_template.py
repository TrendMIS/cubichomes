# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    video_url = fields.Char()
    video_code = fields.Char(compute='_compute_video_code')
    layout_plan_ids = fields.Many2many('layout.plan')
    @api.depends('video_url')
    def _compute_video_code(self):
        for rec in self:
            if rec.video_url:
                if '?v=' in rec.video_url:
                    rec.video_code = rec.video_url.split('?v=')[1]
                else:
                    rec.video_code = rec.video_url.split('be/')[1]
            else:
                rec.video_code = False
