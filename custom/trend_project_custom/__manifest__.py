# -*- coding: utf-8 -*-
{
    'name': "Trend Project Custom",

    'summary': """""",

    'author': "Trend Development Team",

    # any module necessary for this one to work correctly
    'depends': ['sale_project', 'documents', 'sales_amount_discount'],

    # always loaded
    'data': [
        'views/project_project.xml',
        'views/project_milestone.xml',
        'views/project_task.xml',
        'views/account_payment.xml',
    ],
}
