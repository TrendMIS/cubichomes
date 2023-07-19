# -*- coding: utf-8 -*-
{
    'name': "Website Product",

    'summary': """""",

    'author': "Trend Development Team",
    # any module necessary for this one to work correctly
    'depends': ['trend_advanced_search_website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/layout_plan.xml',
        'views/product_card.xml',
        'views/product_template.xml',
        'views/variant_templates.xml',
    ],
}
