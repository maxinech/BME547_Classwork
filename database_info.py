from pymodm import MongoModel, fields, connect


class Patient(MongoModel):
    name = fields.CharField()
    patient_id = fields.IntegerField(primary_key=True)
    blood_type = fields.CharField()
    tests = fields.DictField()
