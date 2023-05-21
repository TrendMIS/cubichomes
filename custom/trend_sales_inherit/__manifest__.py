# -*- coding: utf-8 -*-
{
    'name': "Trend Sales Inherit",

    'summary': """""",

    'author': "Trend Development Team",
    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'sale_project'],

    # always loaded
    'data': [
        'views/sale_order.xml',
        'views/product_template_views.xml',
        'report/sale_report.xml',
    ],
}
