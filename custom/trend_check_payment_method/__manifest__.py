# -*- coding: utf-8 -*-
{
    'name': "Trend Check Payment Method",

    'summary': """""",

    'author': "Trend Development Team",

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'data/account_method.xml',
        'views/account_payment.xml',
        'report/check_report.xml',
    ],
}
