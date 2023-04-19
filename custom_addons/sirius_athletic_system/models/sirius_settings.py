# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SubdivisionKumite(models.Model):
    _name = 'sirius.settings.subdivision'
    _order= 'category_div,name'

    atleta_ids=fields.One2many(
        comodel_name = 'sirius.athlete',  # related model
        inverse_name = 'subdivision_id',  # field for "this" on related model
        string='Atletas',invisible = True)

    name = fields.Char(string='Subdivisión de Peso')
    category_div = fields.Selection([
        ('infantilA','Infantil 6-7 Años'),
        ('infantilB','Infantil 8-9 Años'),
        ('infantilC','Sub-12 (10-11 Años)'),
        ('sub14','Sub-14 (12-13 Años)'),
        ('cadete','Cadete (14-15 Años)'),
        ('junior','Junior (16-17 Años)'),
        ('sub21','Sub-21 (18-20 Años)'),
        ('senior','Senior (+18 Años)'),
    ])
    sex_div = fields.Selection([
        ('male','Masculino'),
        ('female','Femenino'),
    ],string = 'Genero')

    kata_div=fields.Boolean(string='Kata')

