import pytest


@pytest.mark.parametrize("input_dictionary, expected", [
    ({"name": "David", "id": 1, "blood_type": "O+"}, 200),
    ({"name": "David"}, 400),
    ({"name": "David", "id": 0, "other": "O+"}, 400),
    ({"nxme": "David", "id": 1, "blood_type": "O+"}, 400),
    ({"name": "David", "id": 1, "blood_type": "O+", "other": 2}, 200),
    ({"name": "David", "id": "2", "blood_type": "O+"}, 400),
    (["David", 1, "O+"], 400)
])
def test_validate_server_input(input_dictionary, expected):
    from health_db_server import validate_server_input
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    answer, status_code = validate_server_input(input_dictionary,
                                                expected_keys,
                                                expected_types)
    assert status_code == expected


@pytest.mark.parametrize("in_data, expected", [
    ({"name": "David", "id": 1, "blood_type": "O+"}, 200),
    ({"name": "David"}, 400)
])
def test_new_patient_driver(in_data, expected):
    from health_db_server import new_patient_driver
    answer, status_code = new_patient_driver(in_data)
    assert status_code, expected


@pytest.mark.parametrize("patient_name, id_no, blood_type", [
    ("David", 1, "O+")
])
def test_add_patient_to_db(patient_name, id_no, blood_type):
    from health_db_server import add_patient_to_db, db
    add_patient_to_db(patient_name, id_no, blood_type)
    answer = db[-1]
    expected = {"name": patient_name, "id": id_no, "blood_type": blood_type,
                "tests": {}}
    assert answer == expected


@pytest.mark.parametrize("patient_id, expected, expected_status_code", [
    ("101", 101, 200),
    ("15.1", "Patient_id was not an integer", 400),
    ("david", "Patient_id was not an integer", 400),
])
def test_validate_convert_patient_id(patient_id, expected,
                                     expected_status_code):
    from health_db_server import validate_convert_patient_id
    answer, status_code = validate_convert_patient_id(patient_id)
    assert status_code == expected_status_code
    assert answer == expected


def test_get_patient_tests_from_database_find_patient():
    from health_db_server import add_patient_to_db, \
        get_patient_tests_from_database
    add_patient_to_db("Eugene", 555, "A+")
    answer, status_code = get_patient_tests_from_database(555)
    assert answer == {}
    assert status_code == 200


def test_get_patient_tests_from_database_bad_patient():
    from health_db_server import get_patient_tests_from_database
    answer, status_code = get_patient_tests_from_database(444)
    assert answer == "Patient_id 444 was not found"
    assert status_code == 400


@pytest.mark.parametrize("new_patient_id, search_id_string, expected_code", [
    (123, "123", 200),
    (None, "Donna", 400),
    (None, "234", 400)
])
def test_get_results_driver(new_patient_id, search_id_string, expected_code):
    from health_db_server import get_results_driver, add_patient_to_db
    if new_patient_id is not None:
        add_patient_to_db("Test Patient Name", new_patient_id, "O+")
    answer, status_code = get_results_driver(search_id_string)
    assert status_code, expected_code


@pytest.mark.parametrize("new_patient_id, patient_id_int, test_name,"
                         "test_result, expected_code", [
                          (345, 345, "HDL", 50, 200),
                          (None, 345, "LDL", 40, 200),
                          (None, 345, "HDL", 51, 200),
                          (None, 3456, "HDL", 50, 400),
                         ])
def test_add_test_to_patient(new_patient_id, patient_id_int, test_name,
                             test_result, expected_code):
    from health_db_server import add_test_to_patient, add_patient_to_db
    if new_patient_id is not None:
        add_patient_to_db("Test Patient Name", new_patient_id, "O+")
    test_data = {"id": patient_id_int, "test_name": test_name,
                 "test_result": test_result}
    answer, status_code = add_test_to_patient(test_data)
    assert status_code == expected_code


@pytest.mark.parametrize("new_patient_id, test_data, expected_code", [
    (345, {"id": 345, "test_name": "HDL", "test_result": 50}, 200),
    (None, {"ixd": 345, "test_name": "HDL", "test_result": 50}, 400),
    (None, {"id": "junk", "test_name": "HDL", "test_result": 50}, 400),
    (None, {"id": 345, "test_name": "HDL", "test_result": 51}, 200),
    (None, {"id": 3456, "test_name": "HDL", "test_result": 50}, 400),
])
def test_add_test_driver(new_patient_id, test_data, expected_code):
    from health_db_server import add_test_driver, add_patient_to_db
    if new_patient_id is not None:
        add_patient_to_db("Test Patient Name", new_patient_id, "O+")
    answer, status_code = add_test_driver(test_data)
    assert status_code == expected_code
