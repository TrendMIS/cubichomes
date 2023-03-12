# -*- coding: utf-8 -*-
{
    'name': "Trend Sales Invoice Amount Discount",
    'summary': "Trend Sales Invoice Amount Discount",
    'description': """
        This module edit on invoice module to add the following : \n
            Amount Discount to apply on lines.
     """,
    'author': "Trend Development Team",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_inherit.xml',
        # 'views/account_move.xml',
        'views/res_partner.xml',
        'report/sale_quotation_inherit.xml',
        'report/invoice_report.xml',
    ],
}
