from pymodm import connect

connect("mongodb+srv://maxinech:Mikan54669@bme547."
        "wdo8g.mongodb.net/health_db?retryWrites=true&w=majority")


def test_add_patient_to_db():
    from health_db_server import add_patient_to_db
    patient_name = "Test Patient"
    patient_id = 2
    blood_type = "O+"
    answer = add_patient_to_db(patient_name, patient_id, blood_type)
    answer.delete()  # clean up on database, won't delete locally
    assert answer.name == patient_name
    assert answer.patient_id == patient_id
