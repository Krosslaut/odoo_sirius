# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Atleta(models.Model):
    _name = 'sirius.athlete'
    _description = 'Atleta'
    _inherits = {
        'res.partner': 'partner_id',
    }
    _order = 'name'

    partner_id = fields.Many2one(
        'res.partner',
        required=True,
        ondelete='cascade',
        auto_join=True,
        string="Usuario Relacionado",
        help="Usuario relacionado con los datos de atleta")

    is_national=fields.Boolean('Selección Nacional')
    is_state=fields.Boolean('Selección Estadal')
    is_grown=fields.Boolean('Atleta en Desarrollo')

    grade=fields.Selection([
        ('grade10','10mo Kyu'),
        ('grade11','9no Kyu'),
        ('grade12','8vo Kyu'),
        ('grade13','7mo Kyu'),
        ('grade14','6to Kyu'),
        ('grade15','5to Kyu'),
        ('grade16','4to Kyu'),
        ('grade17','3er Kyu'),
        ('grade18','2do Kyu'),
        ('grade19','1er Kyu'),
        ('grade20','Shodan Ho'),
        ('grade21','1er Dan'),
        ('grade22','2do Dan'),
        ('grade23','3er Dan'),
        ('grade24','4to Dan'),
        ('grade25','5to Dan'),
        ('grade26','6to Dan'),
        ('grade27','7mo Dan'),
        ('grade28','8vo Dan'),
        ('grade29','9no Dan'),
        ('grade30','10mo Dan'),
    ],'Grado')

    grade_code=fields.Char('Número de Acta de Grado')

    legal_rep = fields.Selection([
        ('padre','Padre'),
        ('madre','Madre'),
        ('ambos','Ambos'),
        ('otro','Otro')
    ],string = 'Representante Legal', default='ambos',)

    father_name = fields.Char(string = "Nombre del Padre", help="Nombre y apellido del padre")
    father_bdate = fields.Date(string = "F. de Nac. del Padre")
    father_vat = fields.Char(string = "Cédula del Padre")
    father_tlf = fields.Char(string = "Teléfono del Padre")
    father_mail = fields.Char(string = "Correo Electrónico del Padre")
    father_career = fields.Char(string= "Profesión del Padre")
    
    mother_name = fields.Char(string = "Nombre de la Madre", help="Nombre y apellido de la madre")
    mother_bdate = fields.Date(string = "F. de Nac. de la Madre")
    mother_vat = fields.Char(string = "Cédula de la Madre")
    mother_tlf = fields.Char(string = "Teléfono de la Madre")
    mother_mail = fields.Char(string = "Correo Electrónico de la Madre")
    mother_career = fields.Char(string= "Profesión de la Madre")
    
    legal_rep_other = fields.Char('Descripción')

    other_name = fields.Char(string = "Nombre de la Madre", help="Nombre y apellido de la madre")
    other_bdate = fields.Date(string = "F. de Nac. de la Madre")
    other_vat = fields.Char(string = "Cédula de la Madre")
    other_tlf = fields.Char(string = "Teléfono de la Madre")
    other_mail = fields.Char(string = "Correo Electrónico de la Madre")
    other_career = fields.Char(string= "Profesión de la Madre")

    dojo_id = fields.Many2one(
        'sirius.dojo',  # related model
        string='Dojo',)
    
    sensei_id = fields.Many2one(
        'sirius.sensei',  # related model
        string='Sensei',)
    
    

