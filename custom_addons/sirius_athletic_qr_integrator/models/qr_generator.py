# -*- coding: utf-8 -*-
import qrcode
import base64
from io import BytesIO

from odoo import models, fields, api, _, SUPERUSER_ID
from odoo.exceptions import UserError
   
class AtletaQR(models.Model):
    _inherit = "sirius.athlete"
        
    def generate_qr_code(self):
        qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=10,
                border=4,
                )
        qr.add_data(str(self.name)+'\n'+str(self.vat)+'\n'+str(self.athlete_category)+'\n'+str(self.grade)+'\n'+str(self.sensei_id.name)+'\n'+str(self.dojo_id.name))
        qr.make(fit=True)
        img = qr.make_image()
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_img = base64.b64encode(temp.getvalue())
        self.qr_code = qr_img
    
    qr_code = fields.Binary("Código QR", compute = "generate_qr_code")

class SenseiQR(models.Model):
    _inherit = "sirius.sensei"
    
    def generate_qr_code(self):
        qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=10,
                border=4,
                )
        qr.add_data(str(self.name)+' '+str(self.vat))
        qr.make(fit=True)
        img = qr.make_image()
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_img = base64.b64encode(temp.getvalue())
        self.qr_code = qr_img
    
    qr_code = fields.Binary("Código QR", compute = "generate_qr_code")