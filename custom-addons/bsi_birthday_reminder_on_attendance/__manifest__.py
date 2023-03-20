# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2021-today Botspot Infoware Pvt ltd'<www.botspotinfoware.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

{
    'name'         : "Birthday Reminder On Attendance",
    'author'       : 'Botspot Infoware Pvt. Ltd.',
    'category'     : 'Attendances',
    'summary'      : """Colleagues can wish 'Happy Birthday' from the 'Attendance Check-In'""",
    'website'      : 'https://www.botspotinfoware.com',
    'company'      : 'Botspot Infoware Pvt. Ltd.',
    'maintainer'   : 'Botspot Infoware Pvt. Ltd.',
    'description'  : """ According to the employee's date of birth, whenever other employees are doing check-in on same day than they will know the employee's birthday demo the attendance screen and other employees will wish him/her by just clicking a button into the attendance check-in screen.""",
    'version'      : '1.0',
    'depends'      : ['base', 'hr_attendance'],
    'data'         : [],
    "images"       : ['static/description/Birthday Reminder On Att.gif'],
    "qweb"         :  [],
    'license'      : 'LGPL-3',
    'installable'  : True,
    'application'  : True,
    'assets': {
        'web.assets_backend': [
            'bsi_birthday_reminder_on_attendance/static/src/js/greeting_message.js',
        ],
    },
    'auto_install' : False,
}
