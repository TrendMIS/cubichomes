# -*- coding: utf-8 -*-
{
    'name': "Trend Amount Words",

    'summary': """Convert Amount To Words""",

    'author': "Trend Development Team",

    # any module necessary for this one to work correctly
    'depends': ['account', 'sale'],

    # always loaded
    'data': [
        'report/invoice_report.xml',
        'report/sale_report.xml',
        'views/account_move.xml',
        'views/sale_order.xml',
    ],
}
