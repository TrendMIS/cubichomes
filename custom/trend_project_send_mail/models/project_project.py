# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'

    def send_mail(self):
        return {
            'name': 'Send Mail',
            'res_model': 'send.mail.wizard',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_project_id': self.id},
            'view_id': self.env.ref('trend_project_send_mail.send_mail_wizard_view_form').id
        }

