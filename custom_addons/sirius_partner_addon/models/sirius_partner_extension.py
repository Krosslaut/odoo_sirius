# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class sirius_partner_addon(models.Model):
    _inherit = 'res.partner'

#------------------- Funciones de Definicion de nombre -------------------------------
    @api.model
    def _get_computed_name(self, middle_name, first_name):
        """Compute the 'name' field according to splitted data.
        You can override this method to change the order of lastname and
        firstname the computed name"""
        for rec in self:
            return " ".join(p for p in (first_name, middle_name) if p)
    
    @api.depends("first_name", "middle_name")
    def _compute_name(self):
        """Write the 'name' field according to splitted data."""
        for record in self:
            record.name = record._get_computed_name(record.middle_name, record.first_name)

#----------------- Funcion de definicion de edad y cumpleaños ---------------------------------------
    @api.depends('birth_date')
    def _compute_age(self):
        today = datetime.now()
        for rec in self:
            age = ''
            today_is_birthday = False
            if rec.birth_date:
                end_data = fields.Datetime.now()
                delta = relativedelta(end_data, rec.birth_date)
                age = str(delta.years)

                if today.strftime('%m')==rec.birth_date.strftime('%m') and today.strftime('%d')==rec.birth_date.strftime('%d'):
                    today_is_birthday = True
            rec.age = age
            rec.today_is_birthday = today_is_birthday

#-------------------- Funciones para generar el código de Usuario ---------------------
    @api.model
    def create(self, vals):
        if vals.get('reg_number','New')=='New':
            vals['reg_number'] = self.env['ir.sequence'].next_by_code('res.partner')or 'New'
        result=super(sirius_partner_addon,self).create(vals)
        return result

    @api.model
    def _user_code_atributes(self, first_name, middle_name, birth_date, reg_number):
        if self.first_name and self.middle_name:
            code_names = "".join(n for n in(first_name[0].upper(), middle_name[0].upper()))
        else:
            code_names=str("XX")
        if self.birth_date:
            code_birth_date = birth_date.strftime('%d') + birth_date.strftime('%m') + birth_date.strftime('%y')
        else:
            code_birth_date = str("000000")
        return "-".join(p for p in (str(reg_number),code_names,code_birth_date))

    @api.depends("first_name","middle_name","birth_date")
    def _user_code(self):
        for rec in self:
            rec.user_code = rec._user_code_atributes(rec.first_name,rec.middle_name,rec.birth_date,rec.reg_number)

#-------------------- Datos de Identificación ----------------------------------------
    name = fields.Char(
        compute="_compute_name",
        required=False,
        store=True,
        readonly=False,)

    first_name = fields.Char(string = 'Primer nombre')
    second_name = fields.Char(string = 'Segundo nombre')
    middle_name = fields.Char(string = 'Primer apellido')
    last_name = fields.Char(string = 'Segundo apellido')

    birth_date = fields.Date()
    today_is_birthday = fields.Boolean(string='Birthday Today', compute='_compute_age')
    age = fields.Char(string="Edad", compute="_compute_age")
    
    vat_exp_date=fields.Date(string='FdV Cédula')
    vat_pic=fields.Image(string='Foto de Cédula')
    passport = fields.Char(string = 'Pasaporte')
    passport_exp_date=fields.Date(string='FdV Pasaporte')
    passport_pic=fields.Image(string='Foto de Pasaporte')
    
    sex = fields.Selection([
        ('female','Femenino'),
        ('male','Masculino'),
        ('other','Otro'),
    ],string = 'Sexo', default="male", tracking=True)

    reg_number=fields.Char(default="New",readonly=True, copy=False)
    user_code=fields.Char(compute="_user_code", string="Código de Usuario", readonly=True, store=True)
    
    #-------------------- Datos de Contacto y Redes Sociales -----------------------------
    instagram = fields.Char('Instagram')
    facebook = fields.Char('Facebook')
    tiktok = fields.Char('TikTok')
    zoom = fields.Char('Zoom')

    



    