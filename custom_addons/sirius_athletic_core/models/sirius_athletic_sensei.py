# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Atleta(models.Model):
    _name = 'sirius.sensei'
    _description = 'Sensei'
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
        help="Usuario relacionado con los datos de Sensei")
    
    dojo_ids=fields.One2many(
        comodel_name = 'sirius.dojo',  # related model
        inverse_name = 'sensei_id',  # field for "this" on related model
        string='Dojos',)
    
    atleta_ids=fields.One2many(
        comodel_name = 'sirius.athlete',  # related model
        inverse_name = 'sensei_id',  # field for "this" on related model
        string='Atletas',)