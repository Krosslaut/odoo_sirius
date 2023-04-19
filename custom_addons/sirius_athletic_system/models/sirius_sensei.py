# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sensei(models.Model):
    _name = 'sirius.sensei'
    _description = 'Base de datos de los sensei registrados en el dojo'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order='name'

    first_name = fields.Char(string = 'Primer nombre')
    second_name = fields.Char(string = 'Segundo nombre')
    middle_name = fields.Char(string = 'Primer apellido')
    last_name = fields.Char(string = 'Segundo apellido')

    son_cty = fields.Integer(string="Cantidad de hijos")

    partner_id = fields.Many2one(
        'res.partner',
        delegate=True,
        ondelete='cascade',
        required=True)
    
    user_id = fields.Many2one(
        'res.users', 
        string='Usuario', 
        ondelete="cascade",
        default = lambda self: self.env.user,
        required=False)

    organizacion_id = fields.Many2one(
        'sirius.organizacion',
        string='Organización',)
    
    asociacion_id = fields.Many2one(
        'sirius.asociacion',
        string='Asociacion',)    
        
    dojo_ids=fields.One2many(
        comodel_name = 'sirius.dojo',  # related model
        inverse_name = 'sensei_id',  # field for "this" on related model
        string='Dojos',)
    
    atleta_ids=fields.One2many(
        comodel_name = 'sirius.athlete',  # related model
        inverse_name = 'sensei_id',  # field for "this" on related model
        string='Atletas',)

    @api.onchange("first_name","second_name","middle_name","last_name")  
    def _onchange_name (self):
        if not self.second_name:
            if not self.last_name:
                self.name = str(self.first_name)+' '+str(self.middle_name)
                return
            self.name = str(self.first_name)+ ' '+str(self.middle_name)+' '+str(self.last_name[0].upper())+ '.'
            return
        if not self.last_name:
            self.name =str(self.first_name)+ ' ' +str(self.second_name[0].upper())+ '. '+str(self.middle_name)
            return
        self.name =str(self.first_name)+ ' ' +str(self.second_name[0].upper())+ '. '+str(self.middle_name)+' '+str(self.last_name[0].upper())+ '.'
        return
    
    def create_sensei_user(self):
        user_group = self.env.ref("sirius_athletic_system.sirius_group_sensei")
        user_type = self.env.ref("base.group_user")
        users_res = self.env['res.users']
        for record in self:
            user_id = users_res.create({
                'name': record.name,
                'partner_id': record.partner_id.id,
                'login': record.email,
                'groups_id': user_group and user_type,
                'tz': self._context.get('tz'),
            })
            record.user_id = user_id