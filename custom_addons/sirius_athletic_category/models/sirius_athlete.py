# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class AthleteCategory(models.Model):
    _inherit = "sirius.athlete"

    category_ids = fields.Many2many(
        'sirius.category',
        'rel_cat_athlete',
        'cat_id',
        'athlete_id',
        string='Categorias',
        domain = "[('min_age','<=','age'),('max_age','>=','age')]")