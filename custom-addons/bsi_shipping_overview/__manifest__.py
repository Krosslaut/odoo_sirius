# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2021-today Botspot Infoware Pvt. Ltd. <www.botspotinfoware.com>
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
    'name'        : "Total Shipping Count/Amount",
    'author'      : 'Botspot Infoware Pvt. Ltd.',
    'category'    : 'Delivery',
    'summary'     : "Helps to get total shipping method amount and the number of successful delivery.",
    'website'     : 'https://www.botspotinfoware.com',
    'company'     : 'Botspot Infoware Pvt. Ltd.',
    'maintainer'  : 'Botspot Infoware Pvt. Ltd.',
    'description' : """Helps to get total shipping method amount and the number of successful delivery.""",
    'version'     : '1.0',
    'depends'     : ['base', 'sale', 'delivery'],
    'data'        : [
                     "security/ir.model.access.csv",
                     "views/delivery_view.xml",
                    ],
    "images"      :  ['static/description/Total Shipping Count Amount.gif'],
    'qweb'        : [],
    'license'     : 'LGPL-3',
    'installable' : True,
    'application' : True,
    'auto_install': False,
}
