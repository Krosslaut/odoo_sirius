# -*- coding: utf-8 -*-
{
    'name': "Sirius Category Handler",

    'summary': """
        Categorias para atletas de la plataforma Sirius""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ricardo Meneses",
    'website': "http://www.SiriusMediaDRM.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sirius_athletic_system'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sirius_athlete_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
