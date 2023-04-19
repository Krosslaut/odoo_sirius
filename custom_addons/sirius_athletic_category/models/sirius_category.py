# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SiriusCategory(models.Model):
    _name = 'sirius.category'
    _description = 'Categorías atleticas estandar para Karate'
    _order = "id desc"

    @api.depends('category_age')
    def _range_age(self):
        for rec in self:
            if rec.category_age == '0':
                rec.min_age = 0
                rec.max_age = 5
            if rec.category_age == '1':
                rec.min_age = 6
                rec.max_age = 6
            if rec.category_age == '2':
                rec.min_age = 7
                rec.max_age = 7
            if rec.category_age == '3':
                rec.min_age = 8
                rec.max_age = 8
            if rec.category_age == '4':
                rec.min_age = 9
                rec.max_age = 9
            if rec.category_age == '5':
                rec.min_age = 10
                rec.max_age = 11
            if rec.category_age == '6':
                rec.min_age = 12
                rec.max_age = 13
            if rec.category_age == '7':
                rec.min_age = 14
                rec.max_age = 15
            if rec.category_age == '8':
                rec.min_age = 16
                rec.max_age = 17
            if rec.category_age == '9':
                rec.min_age = 18
                rec.max_age = 20
            if rec.category_age == '10':
                rec.min_age = 18
                rec.max_age = 100
        return
    
    @api.depends('category_age')
    def _get_category(self):
        for rec in self:
            if rec.category_age:
                rec.category_name = 'cat_'+ str(rec.category_age)
            else:
                rec.category_name = False
    
    READONLY_STATES = {'cancel': [('readonly', True)], 'done': [('readonly', True)]}

    name = fields.Char('Categoría')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='State', default='draft', required=True, copy=False, states=READONLY_STATES)

    athlete_ids = fields.Many2many('sirius.athlete', string = "Atletas")
    
    is_senior=fields.Boolean('Senior')
    is_sub21=fields.Boolean('Sub21')
    
    category_age = fields.Selection([
        ('0','Menos de 5 años'),
        ('1','6 años'),
        ('2','7 años'),
        ('3','8 años'),
        ('4','9 años'),
        ('5','10-11 años'),
        ('6','12-13 años'),
        ('7','14-15 años'),
        ('8','16-17 años'),
        ('9','18-20 años'),
        ('10','Adulto'),
    ], string="Edad")
    
    category_name = fields.Selection([
        ('cat_0',"Semillero"),
        ('cat_1',"Infantil 6"),
        ('cat_2',"Infantil 7"),
        ('cat_3',"Infantil 8"),
        ('cat_4',"Infantil 9"),
        ('cat_5',"Sub12"),
        ('cat_6',"Sub14"),
        ('cat_7',"Cadete"),
        ('cat_8',"Junior"),
        ('cat_9',"Sub21"),
        ('cat_10',"Senior"),
    ],string='Categoría', compute='_get_category', store=True)

    min_age = fields.Integer(compute='_range_age', stored=True, string="Edad mínima")
    max_age = fields.Integer(compute='_range_age',stored=True, string="Edad maxima")
    
    category_sex = fields.Selection([
        ('fem','Femenino'),
        ('masc','Masculino'),
    ], string='Sexo de la Categoría')

    disciplina=fields.Selection([
        ('1_kai','Kata Individual'),
        ('2_kae','Kata Equipo'),
        ('3_kui','Kumite Individual'),
        ('4_kue','Kumite Equipo'),
    ],string="Disciplina")

    subdiv=fields.Char('Subdivisión', help='Subdivisión de peso aplicable a los atletas de kumite')

    description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
