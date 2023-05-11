import xmlrpc.client

url = 'http://127.0.0.1:8069'
db = 'vertical_hospital'
username = 'jeremiasp96@gamil.com'
password = 'admin'


common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

#authentication
uid = common.authenticate(db, username, password, {})

if uid:
    
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    ids = models.execute_kw(db, uid, password, 'vhospital.patient','search', [[['name_seq', '=', 'PA00001']]])
    patients = models.execute_kw(db, uid, password, 'vhospital.patient','read', [ids], {'name_seq': ['patient_name','patient_name', 'patient_last_name', 'patient_dni','state']})

    print("patient", patients)
else:
    print("authentication failed")