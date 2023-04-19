# -*- coding: utf-8 -*-
{
    'name': "Sirius Athletic Core",
    '_name': "sirius_athletic_core",

    'summary': """
        Moduo núcleo de la plataforma de gestión atletica""",

    'description': """
        En el presente módulo se permiten registrar todos los datos de los miembros que hacen vida en el
        karate, así como los datos de las instituciones que los respaldan.

        Posee las siguientes bondades:
        -   Plantilla de Atletas
        -   Plantilla de Sensei
        -   Listado de Dojos registrados
        -   Información relevante para el director técnico
        -   Reportes de progreso y status de los atletas
        -   Ranking de los atletas inscritos en el sistema
        -   Impresión de documentos de la organización (carnets, planillas, fichas técnicas, entre otras).
    """,

    'author': "Sirius Media DRM, C.A.",
    'website': "http://www.siriusmediaDRM.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '16.1.2',

    # any module necessary for this one to work correctly
    'depends': ['mail','l10n_ve_dpt','sirius_partner_addon','sirius_medical_addon'],

    'application': True,

    # always loaded
    'data': [
        'security/sirius_athletic_security.xml',
        'security/ir.model.access.csv',
        'views/sirius_menu_view.xml',
        'views/sirius_athlete_view.xml',
        'views/sirius_partner_view.xml',
        
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
