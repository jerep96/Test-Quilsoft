{
'name': 'Vertical Hospital V1',
'version': '1.0',
'author': 'Jeremias Palacios',
'category': 'Medical',
'summary': 'Odoo module for managing hospital patients',
'sequence': '1',
'license': 'AGPL-3',
'depends': ['base','mail'],
'data': [
    'security/ir.model.access.csv',
    'data/sequence.xml',
    'views/patient.xml',
    'views/treatments.xml',
    'reports/report.xml',
    'reports/patient_report.xml'
],
'demo': [],
'installable': True,
'application': True,
}