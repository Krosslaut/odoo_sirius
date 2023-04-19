# -*- coding: utf-8 -*-

from odoo import fields, models, api
   
class Medidas(models.Model):
    _name='sirius.measure'
    _description="Medidas"
    _order = 'athlete_id'

    name = fields.Date(string='Fecha de Pesaje')
    athlete_height = fields.Float(string = 'Altura')
    athlete_weight = fields.Float(string = 'Peso')
    waist_diam = fields.Float(string = 'Diametro de Cintura')
    plexus_diam = fields.Float(string = 'Diametro de Plexo')
    wingspan = fields.Float(string = 'Envergadura')
    height_wf = fields.Float(string = 'Altura Espina Iliaca')
    shoe_size = fields.Integer(string = 'Talla de Calzado')
    
    athlete_id = fields.Many2one(
        'sirius.athlete',
        string='Atletas',
        default=lambda self: self.env[
            'sirius.athlete'].partner_id
    )
    dojo_related = fields.Many2one(
        related = "athlete_id.dojo_id",
        string = "Dojo",
        store = "True"
    )

    

    