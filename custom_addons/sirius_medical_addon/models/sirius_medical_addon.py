# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    blood_group = fields.Selection([
        ('A+', 'A+'),('A-', 'A-'),
        ('B+', 'B+'),('B-', 'B-'),
        ('AB+', 'AB+'),('AB-', 'AB-'),
        ('O+', 'O+'),('O-', 'O-')], string='Grupo Sanguineo')
    is_allergic = fields.Boolean(string = "Alergias", default = False)
    allergy_type = fields.Char(string = "Nombre de la alergia")
    is_injured = fields.Boolean(string = "Traumatismos", default = False)
    need_glass = fields.Boolean(string = "Necesita Lentes", default = False)
    injury_type = fields.Char(string = "Nombre de la lesión")
    medic_ext_data = fields.Text(string = "Información médica adicional", default = "")

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
