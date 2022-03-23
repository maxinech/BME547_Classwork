from pymodm import MongoModel, fields


class Patient(MongoModel):
    """ Description of data to be stored for each patient

    This class derives from the pymodm.MongoModel class and is used to define
    the structure of a document in the database for this server.  Each
    document will have four fields:

    name (CharField) will be a string containing the name of the patient
    patient_id (IntegerField) will contain an integer that is the unique
        patient identifier.  This is the primary key of the database.
    blood_type (Charfield) will contain a string that indicates the blood type
        of the patient
    tests (DictField) will contain a dictionary.  Each key of the dictionary
        will be the name of the test and the value for each key will be a
        list that contains the different results obtained for that specific
        test type.

    """
    name = fields.CharField()
    patient_id = fields.IntegerField(primary_key=True)
    blood_type = fields.CharField()
    tests = fields.DictField()
