# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError
import datetime

class Atleta(models.Model):
    _name = 'sirius.athlete'
    _description = 'Atleta'
    _inherits = {"res.partner": "partner_id"}
    _order = 'name'
    
    first_name = fields.Char(string = 'Primer nombre')
    second_name = fields.Char(string = 'Segundo nombre')
    middle_name = fields.Char(string = 'Primer apellido')
    last_name = fields.Char(string = 'Segundo apellido')

    age=fields.Integer(compute='age_category',store = True, string="Edad del Atleta")
    
    athlete_category=fields.Selection([
        ('category1','Alevín (-6 Años)'),
        ('category2','Infantil (7-9 Años)'),
        ('category3','Sub-12 (10-11 Años)'),
        ('category4','Sub-14 (12-13 Años)'),
        ('category5','Cadete (14-15 Años)'),
        ('category6','Junior (16-17 Años)'),
        ('category7','Sub-21 (18-20 Años)'),
        ('category8','Senior (+18 Años)'),
    ], string= "Categoría del Atleta",readonly=True)

    partner_id = fields.Many2one(
        'res.partner',
        ondelete='cascade',
        required=True)
    
    user_id = fields.Many2one(
        'res.users', 
        string='Usuario', 
        ondelete='cascade',
        default = lambda self: self.env.user,
        required=False)
    
    legal_rep = fields.Selection([
        ('padre','Padre'),
        ('madre','Madre'),
        ('ambos','Ambos'),
    ],string = 'Representante Legal', default='ambos',)

    father_name = fields.Char(string = "Nombre del Padre")
    father_birth_date = fields.Date(string = "Fecha de Nacimiento del Padre")
    father_blood_type = fields.Selection([
        ('op','O+'),
        ('on','O-'),
        ('bp','B+'),
        ('bn','B-'),
        ('ap','A+'),
        ('an','A-'),
        ('abp','AB+'),
        ('abn','AB-'),
        ],string = 'Tipo de Sangre del Padre')
    father_vat = fields.Char(string = "Cédula del Padre")
    father_vat_pic = fields.Image('Fotografía de la cédula del Padre')
    father_tlf = fields.Char(string = "Teléfono del Padre")
    father_mail = fields.Char(string = "Correo Electrónico del Padre")
    father_career = fields.Char(string= "Profesión del Padre")
    father_company = fields.Char(string = "Compañía del Padre")
    father_job = fields.Char(string = "Cargo que desempeña el Padre")

    mother_name = fields.Char(string = "Nombre de la madre")
    mother_birth_date = fields.Date(string = "Fecha de Nacimiento de la madre")
    mother_blood_type = fields.Selection([
        ('op','O+'),
        ('on','O-'),
        ('bp','B+'),
        ('bn','B-'),
        ('ap','A+'),
        ('an','A-'),
        ('abp','AB+'),
        ('abn','AB-'),
        ],string = 'Tipo de Sangre de la madre')
    mother_vat = fields.Char(string = "Cédula de la madre")
    mother_vat_pic = fields.Image('Fotografía de la cédula de la madre')
    mother_tlf = fields.Char(string = "Teléfono de la madre")
    mother_mail = fields.Char(string = "Correo Electrónico de la madre")
    mother_career = fields.Char(string= "Profesión de la madre")
    mother_company = fields.Char(string = "Compañía de la madre")
    mother_job = fields.Char(string = "Cargo que desempeña la madre")

    athlete_code=fields.Char(compute="_change_code", string="Código de Atleta", readonly=True)
    grade_code=fields.Char('Número de Acta de Grado')
    
    is_kai=fields.Boolean('Kata Individual')
    is_kae=fields.Boolean('Kata Equipo')
    is_kui=fields.Boolean('Kumite Individual')
    is_kue=fields.Boolean('Kumite Equipo')
    is_national=fields.Boolean('Selección Nacional')
    is_state=fields.Boolean('Selección Estadal')
    is_grown=fields.Boolean('Atleta en Desarrollo')

    subdivision_id=fields.Many2one(
        'sirius.settings.subdivision',  # related model
        string='Subdivisión de Peso')

    asociacion_id = fields.Many2one(
        'sirius.asociacion',  # related model
        string='Asociacion',)

    organizacion_id = fields.Many2one(
        'sirius.organizacion',  # related model
        string='Organización',)

    dojo_id = fields.Many2one(
        'sirius.dojo',  # related model
        string='Dojo',)

    sensei_id = fields.Many2one(
        'sirius.sensei',  # related model
        string='Sensei',)

    measure_ids = fields.One2many(
        comodel_name = 'sirius.measure',  # related model
        inverse_name = 'athlete_id',  # field for "this" on related model
        string='Record del Atleta',
        #options="{'no_open': True, 'no_create': True}"
        )

    state = fields.Selection([
        ('draft','Borrador'),
        ('send','Revisado'),
        ('approved','Confirmado'),
        ('canceled','Cancelado')
    ],string="Etapa", readonly = True, default = 'draft')

    def act_send(self):
        result = self.state = 'send'
        return result and result or False

    def act_approved(self):
        result = self.state = 'approved'
        return result and result or False

    def act_canceled(self):
        self.state = 'canceled'

    def act_set_to_draft(self):
        self.state = 'draft'

#-------------------- Definicion de Name --------------------------------------------  
    @api.onchange('first_name','second_name','middle_name','last_name')
    def _onchange_name (self):
        for record in self:
            a=record.first_name
            b=record.second_name
            c=record.middle_name
            d=record.last_name
            if not b and not d:
                def_name = str(a)+' '+str(c)
                record.name=def_name
            elif not b and d:
                def_name = str(a)+ ' '+str(c)+' '+str(d[0].upper())+ '.'
                record.name=def_name
            elif b and not d:
                def_name =str(a)+' '+str(b[0].upper())+'. '+str(c)
                record.name=def_name
            elif b and d:
                def_name =str(a)+' '+str(b[0].upper())+'. '+str(c)+' '+str(d[0].upper())+'.'
                record.name=def_name
        return
#-------------------- Calculo de Edades y Categoria --------------------------------------------
    @api.depends ("self.date")
    def age_category (self):
        for record in self:
            if record.date and record.date > datetime.date.today():
                raise ValidationError('La fecha de nacimiento no puede ser igual o mayor a la fecha actual')
            elif record.date:
                record.age = (datetime.date.today() - record.date).days/365.25
            if record.age >= 21 :
                record.athlete_category="category8"
            elif record.age >= 18 and record.age < 21:
                record.athlete_category="category7"
            elif record.age == 16 or record.age == 17:
                record.athlete_category="category6"
            elif record.age == 14 or record.age == 15:
                record.athlete_category="category5"
            elif record.age == 12 or record.age == 13:
                record.athlete_category="category4"
            elif record.age == 10 or record.age == 11:
                record.athlete_category="category3"
            elif record.age == 7 or record.age == 8 or record.age == 9:
                record.athlete_category="category2"
            elif record.age <= 6:
                record.athlete_category="category1"

#--------------- Cálculo de Código de Atleta ----------------------------------------
    def _change_code (self):
        for record in self:
            x=record.date
            y=record.first_name
            f=record.second_name
            z=record.middle_name
            g=record.last_name
            if not f:
                f=y
            if not g:
                g=z
            record.athlete_code =  z[0].upper() + y[0].upper() + str('{:02d}'.format(x.day)) + f[0].upper() + g[0].upper() + str('{:02d}'.format(x.month)) + str(x.strftime("%y"))
        return 