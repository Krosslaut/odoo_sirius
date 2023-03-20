# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2023-today Botspot Infoware Pvt. Ltd. <www.botspotinfoware.com>
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
from odoo import api, fields, models, _
from datetime import date


class BsiMergeInvoices(models.TransientModel):
    _name = "bsi.merge.invoices"
    _description = "Bsi Merge Invoices "

    customer = fields.Many2one("res.partner", string="Customer")
    invoice_date = fields.Date(string="Invoice Date")
    account_move_line = fields.Many2many("account.move.line", string="Account")

    def merge_invoice(self):
        for record in self:
            selected_ids = self.env.context.get('active_ids', [])
            selected_records = self.env['account.move'].browse(selected_ids)
            self.account_move_line = selected_records.invoice_line_ids.ids

            move_line_vals = []
            for lines in self.account_move_line:
                line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name,
                        'quantity': lines.quantity, 'price_unit': lines.price_unit})
                move_line_vals.append(line)
            invoice = {'partner_id': record.customer, 'invoice_date': record.invoice_date, 'l10n_in_gst_treatment':
                       record.customer.l10n_in_gst_treatment, 'move_type': 'out_invoice', 'invoice_line_ids': move_line_vals}
            invoice_ids = self.env['account.move'].create(invoice)
            invoice_ids.action_post()

    def merge_andnew(self):
        for record in self:
            selected_ids = self.env.context.get('active_ids', [])
            selected_records = self.env['account.move'].browse(selected_ids)
            if not self.account_move_line:
                self.account_move_line = selected_records.invoice_line_ids.ids
                move_line_vals = []
                for lines in self.account_move_line:
                    line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name,
                            'quantity': lines.quantity, 'price_unit': lines.price_unit})
                    move_line_vals.append(line)
                invoice = {'partner_id': record.customer, 'invoice_date': record.invoice_date, 'l10n_in_gst_treatment':
                           record.customer.l10n_in_gst_treatment, 'move_type': 'out_invoice', 'invoice_line_ids': move_line_vals}
                invoice_ids = self.env['account.move'].create(invoice)
                invoice_ids.action_post()

            else:
                move_line_vals = []
                for lines in self.account_move_line:
                    line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name,
                            'quantity': lines.quantity, 'price_unit': lines.price_unit})
                    move_line_vals.append(line)
                invoice = {'partner_id': record.customer, 'invoice_date': record.invoice_date, 'l10n_in_gst_treatment':
                           record.customer.l10n_in_gst_treatment, 'move_type': 'out_invoice', 'invoice_line_ids': move_line_vals}
                invoice_ids = self.env['account.move'].create(invoice)
                invoice_ids.action_post()

        return {
            'name': "Merge Invoice",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'bsi.merge.invoices',
            'target': 'new',
            'context': {
                    'default_account_move_line': self.account_move_line.ids,
            }
        }

    def merge_andview(self):
        for record in self:
            selected_ids = self.env.context.get('active_ids', [])
            selected_records = self.env['account.move'].browse(selected_ids)
            self.account_move_line = selected_records.invoice_line_ids.ids

            move_line_vals = []
            for lines in self.account_move_line:
                line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name,
                        'quantity': lines.quantity, 'price_unit': lines.price_unit})
                move_line_vals.append(line)
            invoice = {'partner_id': record.customer, 'invoice_date': record.invoice_date, 'l10n_in_gst_treatment':
                       record.customer.l10n_in_gst_treatment, 'move_type': 'out_invoice', 'invoice_line_ids': move_line_vals}
            invoice_ids = self.env['account.move'].create(invoice)
            ir_model_data = self.env['ir.model.data']
            view_id = ir_model_data._xmlid_lookup('account.view_move_form')[2]
            record_id = self.env['account.move'].search(
                [('partner_id', '=', record.customer.id)])

            return {
                'name': record_id.partner_id,
                'view_mode': 'form',
                'view_type': 'form',
                'views': [(view_id, 'form')],
                'view_id': view_id,
                'type': 'ir.actions.act_window',
                'res_model': 'account.move',
                'res_id': invoice_ids.id
            }
