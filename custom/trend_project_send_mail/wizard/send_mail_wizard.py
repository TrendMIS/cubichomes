from odoo import api, fields, models


class SendMailWizard(models.TransientModel):
    _name = 'send.mail.wizard'
    _description = 'Send Mail Wizard'

    project_id = fields.Many2one('project.project')
    partner_ids = fields.Many2many('res.partner')
    text = fields.Text()

    def confirm(self):
        mail = self.env['mail.mail'].create({
            'author_id': self.env.user.partner_id.id,
            'subject': self.project_id.project_ref,
            'recipient_ids': self.partner_ids.ids,
            'body_html': self.text
        })
        mail.send()
