# -*- coding: utf-8 -*-
{
    'name': 'QR Code Dojo App',
    'version': '1.0',
    'category': 'Extra Tools',
    'author': 'Sirius Media Service, C.A.',
    'summary': 'Generate QR Code for Profiles',
    'website': 'https://siriusmediaservice.com',
    'description': """

    """,
    'depends': [
        'sirius_athletic_system',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sirius_athlete_view.xml'
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'installable': True,
    'application': True,
    'license': "AGPL-3",
}
