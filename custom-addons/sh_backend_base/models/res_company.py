# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    enable_web_push_notification = fields.Boolean("Enable Firebase Push Notification")
    enable_bell_notification = fields.Boolean("Enable Bell Notification")
    api_key = fields.Char("Api Key")
    vapid = fields.Char("Vapid",readonly=False)
    config_details = fields.Text("Config Details")
    
class TestSale(models.Model):
    _inherit = 'sale.order'

    def write(self,vals):
        res = super(TestSale,self).write(vals)
        self.env['sh.user.push.notification'].create_user_notification(user=self.env.user,name="Hello there",description="What is your name",res_model="sale.order",res_id=self.id)
        return res
