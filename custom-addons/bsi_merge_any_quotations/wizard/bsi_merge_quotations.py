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


class BsiMergeQuotations(models.TransientModel):
    _name = "bsi.merge.quotations"
    _description = "Bsi Merge Quotations "

    customer = fields.Many2one("res.partner", string="Customer")
    quotations_date = fields.Date(string="Quotations Date")
    sale_order_line = fields.Many2many("sale.order.line", string="Sale")

    def merge_quotations(self):
        for record in self:
            selected_ids = self.env.context.get('active_ids', [])
            selected_records = self.env['sale.order'].browse(selected_ids)
            self.sale_order_line = selected_records.order_line.ids

            move_line_vals = []
            for lines in self.sale_order_line:
                line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name,
                        'product_uom_qty': lines.product_uom_qty, 'price_unit': lines.price_unit})
                move_line_vals.append(line)
            quotation = {'partner_id': record.customer.id, 'date_order': record.quotations_date,
                         'l10n_in_gst_treatment': record.customer.l10n_in_gst_treatment, 'order_line': move_line_vals}
            quotation_ids = self.env['sale.order'].create(quotation)

    def merge_andnew(self):
        for record in self:
            selected_ids = self.env.context.get('active_ids', [])
            selected_records = self.env['sale.order'].browse(selected_ids)
            if not self.sale_order_line:
                self.sale_order_line = selected_records.order_line.ids
                move_line_vals = []
                for lines in self.sale_order_line:
                    line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name,
                            'product_uom_qty': lines.product_uom_qty, 'price_unit': lines.price_unit})
                    move_line_vals.append(line)
                quotation = {'partner_id': record.customer.id, 'date_order': record.quotations_date,
                             'l10n_in_gst_treatment': record.customer.l10n_in_gst_treatment, 'order_line': move_line_vals}
                quotation_ids = self.env['sale.order'].create(quotation)

            else:
                move_line_vals = []
                for lines in self.sale_order_line:
                    line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name,
                            'product_uom_qty': lines.product_uom_qty, 'price_unit': lines.price_unit})
                    move_line_vals.append(line)
                quotation = {'partner_id': record.customer.id, 'date_order': record.quotations_date,
                             'l10n_in_gst_treatment': record.customer.l10n_in_gst_treatment, 'order_line': move_line_vals}
                quotation_ids = self.env['sale.order'].create(quotation)

        return {
            'name': "Merge Quotations",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'bsi.merge.quotations',
            'target': 'new',
            'context': {
                    'default_sale_order_line': self.sale_order_line.ids,
            }
        }

    def merge_andview(self):
        for record in self:
            selected_ids = self.env.context.get('active_ids', [])
            selected_records = self.env['sale.order'].browse(selected_ids)
            self.sale_order_line = selected_records.order_line.ids

            move_line_vals = []
            for lines in self.sale_order_line:
                line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name,
                        'product_uom_qty': lines.product_uom_qty, 'price_unit': lines.price_unit})
                move_line_vals.append(line)
            quotation = {'partner_id': record.customer.id, 'date_order': record.quotations_date,
                         'l10n_in_gst_treatment': record.customer.l10n_in_gst_treatment, 'order_line': move_line_vals}
            quotation_ids = self.env['sale.order'].create(quotation)
            ir_model_data = self.env['ir.model.data']
            view_id = ir_model_data._xmlid_lookup('sale.view_order_form')[2]
            record_id = self.env['sale.order'].search(
                [('partner_id', '=', record.customer.id)])

            return {
                'name': record_id.partner_id,
                'view_mode': 'form',
                'view_type': 'form',
                'views': [(view_id, 'form')],
                'view_id': view_id,
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                'res_id': quotation_ids.id
            }
