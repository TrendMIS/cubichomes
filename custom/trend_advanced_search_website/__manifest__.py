# -*- coding: utf-8 -*-
{
    'name': "Trend Advanced Search Website",

    'summary': """""",

    'author': "Trend Development Team",
    # any module necessary for this one to work correctly
    'depends': ['website_sale', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_attribute.xml',
        'views/product_template.xml',
        'views/homepage_template.xml',
    ],
}
