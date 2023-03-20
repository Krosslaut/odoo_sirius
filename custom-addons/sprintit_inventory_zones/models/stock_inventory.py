# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO Open Source Management Solution
#
#    ODOO Addon module by Sprintit Ltd
#    Copyright (C) 2020 Sprintit Ltd (<http://sprintit.fi>).
#
##############################################################################

from odoo import fields, models,api


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    inventory_zone_id = fields.Many2one('stock.inventory.zone',
                                        string='Inventory Zone',
                                        help="Inventory location zones")


    @api.onchange('inventory_zone_id')
    def _onchange_inventory_zone_id(self):
        if self.inventory_zone_id:
            location = self.env["stock.location"].search([('inventory_zone_id','=',self.inventory_zone_id.id)])
            if location:
                self.write({'location_id' : location[0].id})
            else:
                self.write({'location_id' : []})

    @api.model
    def _get_inventory_fields_write(self):
        fields = super(StockQuant, self)._get_inventory_fields_write()
        fields = fields + ['inventory_zone_id']
        return fields

    # original method from odoo overridden for getting inventory zone straight to sql
    def _get_inventory_lines_values(self):
        # TDE CLEANME: is sql really necessary ? I don't think so
        locations = self.env['stock.location']
        if self.location_ids:
            locations = self.env['stock.location'].search(
                [('id', 'child_of', self.location_ids.ids)])
        else:
            locations = self.env['stock.location'].search(
                [('company_id', '=', self.company_id.id),
                 ('usage', 'in', ['internal', 'transit'])])
        domain = ' stock_quant.location_id in %s AND quantity != 0 AND product_product.active = TRUE'
        args = (tuple(locations.ids),)

        vals = []
        Product = self.env['product.product']
        # Empty recordset of products available in stock_quants
        quant_products = self.env['product.product']

        # If inventory by company
        if self.company_id:
            domain += ' AND stock_quant.company_id = %s'
            args += (self.company_id.id,)
        if self.product_ids:
            domain += ' AND product_id in %s'
            args += (tuple(self.product_ids.ids),)

        # inventory zone
        if self.inventory_zone_id:
            domain += ' AND inventory_zone_id = %s'
            args += (self.inventory_zone_id.id,)
        self.env['stock.quant'].flush(
            ['company_id', 'product_id', 'quantity', 'location_id', 'lot_id',
             'package_id', 'owner_id'])
        self.env['product.product'].flush(['active'])
        self.env.cr.execute("""SELECT product_id, sum(quantity) as product_qty, stock_quant.location_id, lot_id as prod_lot_id, package_id, owner_id as partner_id
                FROM stock_quant
                LEFT JOIN stock_location
                ON stock_location.id = stock_quant.location_id
                LEFT JOIN product_product
                ON product_product.id = stock_quant.product_id
                WHERE %s
                GROUP BY product_id, stock_quant.location_id, lot_id, package_id, partner_id """ % domain,
                            args)

        for product_data in self.env.cr.dictfetchall():
            product_data['company_id'] = self.company_id.id
            product_data['inventory_id'] = self.id
            # replace the None the dictionary by False, because falsy values are tested later on
            for void_field in [item[0] for item in product_data.items() if
                               item[1] is None]:
                product_data[void_field] = False
            product_data['theoretical_qty'] = product_data['product_qty']
            if self.prefill_counted_quantity == 'zero':
                product_data['product_qty'] = 0
            if product_data['product_id']:
                product_data['product_uom_id'] = Product.browse(
                    product_data['product_id']).uom_id.id
                quant_products |= Product.browse(product_data['product_id'])
            vals.append(product_data)
        return vals
