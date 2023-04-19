# -*- coding: utf-8 -*-

from odoo import fields, models, api,_

class Partner(models.Model):
    _inherit = 'res.partner'

#-------------------- Grado  --------------------------------------------
    is_athlete = fields.Boolean(compute="_is_athlete",
                                search="_athlete_search",
                                string="Es Atleta",
                                help="Confirma si el usuario está vinculado a un atleta")
    is_sensei = fields.Boolean(compute="_is_sensei",
                               search="_sensei_search",
                               string="Es Sensei",
                               help="Confirma si el usuario está vinculado a un sensei")
    athlete_id = fields.Many2one('sirius.athletic.athlete',
                                  string="Atleta",
                                  compute="_is_athlete",
                                  readonly=True)
    sensei_id = fields.Many2one('sirius.athletic.sensei',
                                string="Sensei",
                                compute="_is_sensei",
                                readonly=True)
    def _is_athlete(self):
        Athlete=self.env['sirius.athletic.athlete'].sudo()
        for rec in self:
            athlete = Athlete.search([('athlete_id','=', rec.id)], limit=1)
            rec.athlete_id = athlete.id if athlete else False
            rec.is_athlete = True if athlete else False
    def _is_sensei(self):
        Sensei=self.env['sirius.athletic.sensei'].sudo()
        for rec in self:
            sensei = Sensei.search([('sensei_id','=', rec.id)], limit=1)
            rec.sensei_id = sensei.id if sensei else False
            rec.is_sensei = True if sensei else False
    def _athlete_search(self, operator, value):
        athletes = self.env['sirius.athletic.athlete'].sudo().search([])
        return [('id','in', athletes.mapped('partner_id').ids)]
    def _sensei_search(self, operator, value):
        senseis = self.env['sirius.athletic.sensei'].sudo().search([])
        return [('id','in', senseis.mapped('partner_id').ids)]