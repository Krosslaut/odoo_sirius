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
from odoo import api, fields, models, _


class DeliveryCarrier(models.Model):
    _inherit = "delivery.carrier"

    total_shipping_amount = fields.Float(string="Total Shipping Amount", compute='compute_total_shippings_amount')
    total_shippings = fields.Float(string="Total Shipping",compute='compute_total_shippings')

    #compute method use for count total shipping amount
    def compute_total_shippings_amount(self):
        for record in self:
            amttotal = 0.0
            invoice_ids = self.env["account.move"].search([('state', '=', 'posted'),('move_type', '=','out_invoice'),('payment_state' ,'=','paid')])
            for invoice in invoice_ids:
                for line in invoice.invoice_line_ids:
                    if line.product_id.id == record.product_id.id:
                        amttotal += line.price_subtotal
            record.total_shipping_amount = amttotal
               
    #compute method use for count total shipping         
    def compute_total_shippings(self):
        for record in self:
            count=0
            invoice_ids = self.env["account.move"].search([('state', '=', 'posted'),('move_type', '=','out_invoice'),('payment_state' ,'=','paid')])
            for invoice in invoice_ids:
                for line in invoice.invoice_line_ids:
                    if line.product_id.id == record.product_id.id:
                        count += 1
            record.total_shippings = count
                 
