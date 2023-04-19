# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Dojo(models.Model):
    _name = 'sirius.dojo'
    _description = 'Tabla de datos del Dojo'

    name = fields.Char(string='Dojo')
    address = fields.Char(string='Dirección')
    pic = fields.Image('Logo', max_height=300, max_width=300)
    mobile=fields.Char(string='Móvil')
    mail=fields.Char(string='Correo Electrónico')
    instagram=fields.Char(string='Instagram')
    twitter=fields.Char(string='Twitter')
    notes = fields.Text('Notas')

    sensei_id = fields.Many2one(
        'sirius.sensei',
        string='Sensei',
        index=False,)

    atleta_ids=fields.One2many(
        comodel_name = 'sirius.athlete',  # related model
        inverse_name = 'dojo_id',  # field for "this" on related model
        string='Atletas',)