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
from odoo import http, SUPERUSER_ID
import datetime
from datetime import date
from odoo.http import request
import werkzeug


class BirthdayReminder(http.Controller):

    @http.route(['/happy_birthday/<int:employee_id>'], type='http', auth="public", website=True)
    def employee_birthday(self, employee_id, **kwargs):
        channel = {}
        employee = request.env['hr.employee'].browse(employee_id)
        channel_id = request.env['mail.channel'].search([('name', '=', employee.name + ", " + request.env.user.name)])
        if not channel_id:
            channel_dict = request.env['mail.channel'].channel_get([employee.user_id.partner_id.id])
            if channel_dict['id']:
                channel_id = request.env['mail.channel'].browse(channel_dict['id'])

        channel_id.with_context(mail_create_nosubscribe=True).message_post(
            author_id=request.env.user.partner_id.id,
            email_from=request.env.user.email,
            body="Happy Birthday!",
            message_type='comment',
            subtype_id=request.env.ref('mail.mt_comment').id)

        attendance_action_id = request.env.ref('hr_attendance.hr_attendance_action_my_attendances')
        # url = "/web#action=" + str(attendance_action_id.id)
        # return werkzeug.utils.redirect(url)
