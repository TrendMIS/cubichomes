# -*- coding: utf-8 -*-
{
    'name': "Trend Untaxed Amount",

    'summary': """Column in sale order in tree list to show untaxed amount""",

    'author': "Trend Development Team",
    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/sale_order.xml',
        'report/sale_report.xml',
    ],
}
