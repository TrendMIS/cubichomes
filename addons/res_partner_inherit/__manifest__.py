# -*- coding: utf-8 -*-
{
    'name': "Trend Res Partner Inherit",
    'summary': "Trend Res Partner Inherit",
    'description': """
        This module edit on Contacts Module 
     """,
    'author': "Trend Development Team",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}
