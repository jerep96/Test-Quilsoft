# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = 'vhospital.patient'
    _inherit = 'mail.thread'
    _description = 'Patient Record'
    _rec_name = 'patient_name'

    patient_name = fields.Char(string='Name', required=True)
    patient_last_name = fields.Char(string='Last Name', required=True)
    patient_dni = fields.Integer('DNI', required=True, tracking=True, size=8)
    name_seq = fields.Char(string='Order', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    state = fields.Selection([('borrador', 'Borrador'), ('alta', 'Alta'),
                              ('baja', 'Baja')], default='borrador',
                             string="Estado", tracking=True)
    treatments = fields.Many2one('vhospital.treatments', string='Treatments performed')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('vhospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result
    
    @api.constrains('patient_dni')
    def _check_patient_dni(self):
        for rec in self:
            if not isinstance(rec.patient_dni, int):
                raise ValidationError(_("DNI must be an 8-digit number"))