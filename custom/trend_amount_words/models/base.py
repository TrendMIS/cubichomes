from odoo import models, tools
from num2words import num2words


class BaseModelExtend(models.AbstractModel):
    _inherit = 'base'

    def number_to_text(self, number, lang):
        lang = lang.split("_")[0]
        return num2words(number, lang=lang).title()

    @staticmethod
    def is_arabic(lang):
        return "ar" in lang

    def amount_to_text(self, amount, currency, lang):
        self.ensure_one()
        currency_unit_label = 'درهم' if self.is_arabic(lang) else 'AED'
        currency_subunit_label = 'فلسا' if self.is_arabic(lang) else 'Fils'
        split_word = 'و' if self.is_arabic(lang) else 'and'

        formatted = "%.{0}f".format(currency.decimal_places) % amount
        parts = formatted.partition('.')
        integer_value = int(parts[0])
        fractional_value = int(parts[2] or 0)

        amount_words = ' {amt_value} {amt_word}' if self.is_arabic(lang) else ' {amt_word} {amt_value}'

        amount_words = amount_words.format(
            amt_value=self.number_to_text(integer_value, lang),
            amt_word=currency_unit_label,
        )
        if not self.is_zero(amount - integer_value, currency):
            amount_words += ' ' + split_word + tools.ustr(' {amt_value} {amt_word}').format(
                amt_value=self.number_to_text(fractional_value, lang),
                amt_word=currency_subunit_label,
            )
        only = "فقط." if self.is_arabic(lang) else "only."
        return f"{amount_words} {only}"

    def is_zero(self, amount, currency):
        self.ensure_one()
        return tools.float_is_zero(amount, precision_rounding=currency.rounding)
