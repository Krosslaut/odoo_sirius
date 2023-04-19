# -*- coding: utf-8 -*-
{
    'name': "Sirius Athletic System",

    'summary': """
        Modulo especializado para la gestion y organizacion de instituciones deportivas""",

    'description': """
        En el presente módulo se permiten registrar todos los datos de los miembros que hacen vida en el
        karate, así como los datos de las instituciones que los respaldan.

        Posee las siguientes bondades:
        -   Plantilla de Atletas
        -   Plantilla de Sensei
        -   Listado de Dojos registrados
        -   Listado de Organizaciones
        -   Listado de Asociaciones
        -   Información relevante para el director técnico de la organización
        -   Reportes de progreso y status de los atletas
        -   Ranking de los atletas inscritos en el sistema
        -   Impresión de documentos de la organización (carnets, planillas, fichas técnicas, entre otras).
    """,

    'author': "Sirius Media Service, C.A.",
    'website': "http://www.siriusmediaservice.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '14.0.1.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','l10n_ve_dpt','contacts'],

    'application': True,

    # always loaded
    'data': [
        'security/dojo_security.xml',
        'security/ir.model.access.csv',
        'views/sirius_menu_view.xml',
        'views/sirius_athlete_view.xml',
        'views/sirius_record_view.xml',
        'views/sirius_sensei_view.xml',
        'views/sirius_dojo_view.xml',
        'views/sirius_organizacion_view.xml',
        'views/sirius_asociacion_view.xml',
        'views/sirius_settings_view.xml',
        'reports/atleta_profile_report.xml',
        'reports/atleta_carnet_report.xml',
        'reports/atleta_profile_template.xml',
        'reports/atleta_carnet_template.xml',
        #'views/templates.xml'
        
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
