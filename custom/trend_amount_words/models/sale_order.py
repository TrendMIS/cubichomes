# -*- coding: utf-8 -*-

from odoo import fields, models, tools
from num2words import num2words


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    lang = fields.Selection(related='partner_id.lang', string='Language', readonly=False, reaquired=True)

    def number_to_text(self, number):
        if self.lang == 'ar_001':
            lang = 'ar'
        else:
            lang = 'en'
        return num2words(number, lang=lang).title()

    def amount_to_text(self, amount):
        self.ensure_one()
        currency = self.currency_id
        currency_unit_label = 'درهم' if self.lang == 'ar_001' else 'Dirham'
        currency_subunit_label = 'فلسا' if self.lang == 'ar_001' else 'Fils'
        split_word = 'و' if self.lang == 'ar_001' else 'and'

        formatted = "%.{0}f".format(currency.decimal_places) % amount
        parts = formatted.partition('.')
        integer_value = int(parts[0])
        fractional_value = int(parts[2] or 0)

        amount_words = ' ' + tools.ustr('{amt_value} {amt_word}').format(
            amt_value=self.number_to_text(integer_value),
            amt_word=currency_unit_label,
        )
        if not self.is_zero(amount - integer_value, currency):
            amount_words += ' ' + split_word + tools.ustr(' {amt_value} {amt_word}').format(
                amt_value=self.number_to_text(fractional_value),
                amt_word=currency_subunit_label,
            )
        return amount_words

    def is_zero(self, amount, currency):
        self.ensure_one()
        return tools.float_is_zero(amount, precision_rounding=currency.rounding)
