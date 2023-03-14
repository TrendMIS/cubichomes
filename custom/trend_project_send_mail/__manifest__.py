# -*- coding: utf-8 -*-
{
    'name': "Trend Project Send Mail",

    'summary': """""",

    'author': "Trend Development Team",

    # any module necessary for this one to work correctly
    'depends': ['trend_project_custom'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/send_mail_wizard.xml',
        'views/project_project.xml',
    ],
}
