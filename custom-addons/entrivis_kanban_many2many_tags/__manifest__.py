# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2020-Today Entrivis Tech PVT. LTD. (<http://www.entrivistech.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': 'Kanban Many2many Tags',
    'category': 'Web',
    'summary': 'Show pill on the Kanban for Many2many tags.',
    "version": "15.0.1.0.0",
    'description': """Show pill on the Kanban for Many2many tags.""",
    'author': 'Entrivis Tech Pvt. Ltd.',
    'website': 	'https://www.entrivistech.com',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'entrivis_kanban_many2many_tags/static/src/js/kanban_many2many_tags.js',
            'entrivis_kanban_many2many_tags/static/src/scss/style.scss',
        ],
    },
    'installable': True,
    'license': 'LGPL-3',

}
