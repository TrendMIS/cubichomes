# -*- coding: utf-8 -*-
{
    'name': "Website Product Attribute Video",

    'summary': """""",

    'author': "Trend Development Team",
    # any module necessary for this one to work correctly
    'depends': ['trend_advanced_search_website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_card.xml',
        'views/product_template.xml',
        'views/layout_plan.xml',
        'views/variant_templates.xml',
    ],
}
