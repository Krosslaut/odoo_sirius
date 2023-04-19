# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Dojo(models.Model):
    _name = 'sirius.dojo'
    _description = 'Tabla de datos del Dojo'

    name = fields.Char(string='Dojo')
    address = fields.Char(string='Dirección')
    pic = fields.Image('Logo', max_height=50, max_width=50)
    notes = fields.Text('Notas')

    organizacion_id = fields.Many2one(
        'sirius.organizacion',
        string='Organización',
        index=False,)
    
    asociacion_id = fields.Many2one(
        'sirius.asociacion',
        string='Asociacion',
        index=False,)

    sensei_id = fields.Many2one(
        'sirius.sensei',
        string='Sensei',
        index=False,)

    atleta_ids=fields.One2many(
        comodel_name = 'sirius.athlete',  # related model
        inverse_name = 'dojo_id',  # field for "this" on related model
        string='Atletas',)
    

class Organizacion(models.Model):
    _name = 'sirius.organizacion'
    _description = 'Tabla de datos de las organizaciones federadas'

    name = fields.Char(string='Organización')
    direccion = fields.Char(string='Dirección')
    pic = fields.Image('Logo', max_height=50, max_width=50)
    notes = fields.Text('Notas')

    asociacion_ids=fields.Many2many(
        'sirius.asociacion', 
        string="Asociaciones")
    
    dojo_ids=fields.One2many(
        comodel_name = 'sirius.dojo',  # related model
        inverse_name = 'organizacion_id',  # field for "this" on related model
        string='Dojos',)
    
    sensei_ids=fields.One2many(
        comodel_name = 'sirius.sensei',
        inverse_name = 'organizacion_id',
        string = 'Sensei Adscritos',)

    atleta_ids=fields.One2many(
        comodel_name = 'sirius.athlete',  # related model
        inverse_name = 'organizacion_id',  # field for "this" on related model
        string='Atletas',)

class Asociacion(models.Model):
    _name = 'sirius.asociacion'
    _description = 'Asociacion o region a la cual están suscritos los dojos'

    name = fields.Char(string='Asociación')
    direccion = fields.Char(string='Direccion')
    region = fields.Char(string='Región')
    codigo = fields.Integer(string='Numero de registro')
    pic = fields.Image('Logo', max_height=50, max_width=50)
    notes = fields.Text('Notas')
    
    organizacion_ids=fields.Many2many(
        'sirius.organizacion',
        string="Organizaciones")

    dojo_ids=fields.One2many(
        comodel_name = 'sirius.dojo',  # related model
        inverse_name = 'asociacion_id',  # field for "this" on related model
        string='Dojos',)
    
    sensei_ids=fields.One2many(
        comodel_name = 'sirius.sensei',  # related model
        inverse_name = 'asociacion_id',
        string = 'sensei Adscritos',)

    atleta_ids=fields.One2many(
        comodel_name = 'sirius.athlete',  # related model
        inverse_name = 'asociacion_id',  # field for "this" on related model
        string='Atletas',)