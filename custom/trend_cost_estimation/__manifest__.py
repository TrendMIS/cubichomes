# -*- coding: utf-8 -*-
{
    'name': "Trend Cost Estimation",

    'summary': """""",

    'author': "Trend Development Team",
    # any module necessary for this one to work correctly
    'depends': ['project', 'product'],

    # always loaded
    'data': [
        'security/construction_security.xml',
        'security/ir.model.access.csv',
        'views/cost_estimation.xml',
        'views/item_estimation.xml',
        'views/product_template.xml',
    ],
}
