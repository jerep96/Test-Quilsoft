# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class HospitalTreatments(models.Model):
    _name = 'vhospital.treatments'
    _description = 'Treatments Record'
    _rec_name = 'treatments_name'

    treatments_code = fields.Char(string="Treatment code", readonly=True)
    treatments_name = fields.Char(string="Treatment name", readonly=True)
    doctor = fields.Char(string="Treating physician", readonly=True)