# -*- coding: utf-8 -*-

from odoo import fields, models, api,_
from odoo.exceptions import ValidationError
import datetime

class Partner(models.Model):
    _inherit = 'res.partner'

#-------------------- Datos de Identificación ----------------------------------------
    date=fields.Date(string='Fecha de nacimiento', required = "True")

    vat=fields.Char(string='Número de cédula')
    vat_exp_date=fields.Date(string='Fecha de vencimiento de la cédula')
    vat_pic=fields.Image(string='Foto de la cédula')
    passport = fields.Char(string = 'Número de pasaporte')
    passport_exp_date=fields.Date(string='Fecha de vencimiento del pasaporte')
    passport_pic=fields.Image(string='Foto del pasaporte')
    
    sex = fields.Selection([
        ('male','Masculino'),
        ('female','Femenino'),
        ('other','Otro'),
    ],string = 'Sexo')

#--------------------- Datos Médicos ------------------------------------------
    blood_type = fields.Selection([
        ('op','O+'),
        ('on','O-'),
        ('bp','B+'),
        ('bn','B-'),
        ('ap','A+'),
        ('an','A-'),
        ('abp','AB+'),
        ('abn','AB-')
    ],string = 'Tipo de Sangre',)

    is_allergic = fields.Boolean(string = "Posee alergias", default = False)
    allergy_type = fields.Char(string = "Nombre clínico de la alergia", default = "No Posee")
    is_injured = fields.Boolean(string = "Lesiones pasadas", default = False)
    injury_type = fields.Char(string = "Nombre clínico de la lesión", default = "No Posee")
    medic_ext_data = fields.Text(string = "Información médica adicional", default = "")

#-------------------- Datos de Contacto y Redes Sociales -----------------------------
    instagram = fields.Char('Usuario de Instagram')
    facebook = fields.Char('Usuario de Facebook')
    tiktok = fields.Char('Usuario de TikTok')
    zoom = fields.Char('Usuario de Zoom')

#-------------------- Grado  --------------------------------------------
    grade=fields.Selection([
        ('k10','10mo Kyu'),
        ('k9','9no Kyu'),
        ('k8','8vo Kyu'),
        ('k7','7mo Kyu'),
        ('k6','6to Kyu'),
        ('k5','5to Kyu'),
        ('k4','4to Kyu'),
        ('k3','3er Kyu'),
        ('k2','2do Kyu'),
        ('k1','1er Kyu'),
        ('sho','Shodan Ho'),
        ('d1','1er Dan'),
        ('d2','2do Dan'),
        ('d3','3er Dan'),
        ('d4','4to Dan'),
        ('d5','5to Dan'),
        ('d6','6to Dan')
    ],'Grado')

#-----------------------User Type -------------------------
    user_type=fields.Selection([
        ('athlete','Atleta'),
        ('sensei','Entrenador'),
        ('director','Director Técnico'),
        ('user_asoc','Usuario de la Asociación'),
        ('user_org','Usuario de la Organización'),
    ],'Tipo de Usuario')


