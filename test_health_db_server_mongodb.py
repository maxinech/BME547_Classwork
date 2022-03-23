from pymodm import connect
from database_info import Patient

connect("mongodb+srv://maxinech:Mikan54669@bme547."
        "wdo8g.mongodb.net/health_db?retryWrites=true&w=majority")


def test_add_patient_to_db():
    from health_db_server import add_patient_to_db
    patient_name = "Test Patient"
    patient_id = 2
    blood_type = "O+"
    answer = add_patient_to_db(patient_name, patient_id, blood_type)
    answer.delete()
    assert answer.name == patient_name
    assert answer.patient_id == patient_id


def test_add_test_to_patient():
    from health_db_server import add_test_to_patient
    from health_db_server import add_patient_to_db
    patient_name = "Test Patient"
    patient_id = 2
    blood_type = "O+"
    test_patient = add_patient_to_db(patient_name, patient_id, blood_type)
    test_name = "HDL"
    test_result = 65
    new_data = {"id": patient_id, "test_name": test_name,
                "test_result": test_result}
    answer, status_code = add_test_to_patient(new_data)
    find_patient = Patient.objects.raw({"_id": patient_id}).first()
    test_patient.delete()
    assert find_patient.tests[test_name][-1] == test_result
