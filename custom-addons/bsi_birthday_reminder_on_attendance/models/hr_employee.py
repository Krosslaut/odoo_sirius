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
from odoo import models, fields, api, exceptions, _, SUPERUSER_ID
from datetime import datetime, date


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    # When employee is checkin on attendance sheet when see that employee's birthday list and button so click on button we will going to disscuss page.
    def get_todays_employees_birthday_list(self):
        employee_id = self.env['hr.employee'].search([])
        content = ""
        for employee in employee_id:
            message = ""
            users = ""
            current_login = ""
            birthday_body = ""
            if employee.birthday == date.today():
                action_id = self.env.ref('mail.action_discuss')
                users = employee.name
                current_login = self.env.user.name
                name_record = users + ", " + current_login
                birthday_body = "Happy Birthday!"
                mail_message_ids = self.env['mail.message'].search([('body', '=', birthday_body),('record_name', '=', name_record)])
                is_already_message_sent = False
                for mail_message_id in mail_message_ids:
                    message_date = mail_message_id.date.date()
                    if message_date == employee.birthday:
                        is_already_message_sent = True

                past_mail_message_ids = self.env['mail.message'].search([('body', '!=', False), ('record_name', '=', name_record)])
                enable_custome_message = False
                if past_mail_message_ids:
                    enable_custome_message = True

                channel_id = self.env['mail.channel'].search([('name', '=', employee.name + ", " + self.env.user.name)])
                if not channel_id and employee.user_id.partner_id:
                    channel_dict = self.env['mail.channel'].channel_get([employee.user_id.partner_id.id])
                    if channel_dict['id']:
                        channel_id = self.env['mail.channel'].browse(channel_dict['id'])

                if channel_id:
                    url = 'web#action={0}&active_id={1}'.format(action_id.id, channel_id.id)
                    if enable_custome_message:
                        if is_already_message_sent:
                            content += "<tr><td align='left' style=width:40%;'> {0} </td><td></td><td><a href='{1}'><button name='custom_message' id='custom_message' class='btn-primary' align='center' width:40%;'>Custom Birthday Message</button></a></td></tr>".format(employee.name, url)
                        else:
                            content += "<tr><td align='left' style=width:30%;'> {0} </td><td><a href='/happy_birthday/{1}'><button name='happy_birthday' id='happy_birthday' class='btn-primary' align='center' width:40%;'>Say HAPPY BIRTHDAY!</button></a></td><td><a href='{2}'><button name='custom_message' id='custom_message' class='btn-primary' align='center' width:40%;'>Custom Birthday Message</button></a></td></tr>".format(employee.name, employee.id, url)
                    else:
                        content += "<tr><td align='left' style=width:30%;'> {0} </td><td><a href='/happy_birthday/{1}'><button name='happy_birthday' id='happy_birthday' class='btn-primary' align='center' width:40%;'>Say HAPPY BIRTHDAY!</button></a></td><td></td></tr>".format(employee.name, employee.id)

        content = "</br><table class='table' border='1' cellpadding='5' cellspacing='0' style='width:100%; font-size:10px; border-collapse:separate;'> <thead> <tr style='text-align:-webkit-center; background-color:lavender;'> <td><strong>Today's Birthday</strong></td><td><strong>Wish</strong></td><td><strong>Wish</strong></td></tr> </thead> " + content + "<tbody></tbody> </table>"
        return content
