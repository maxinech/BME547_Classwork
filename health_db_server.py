import logging
from flask import Flask, request, jsonify

# Define variable to contain Flask class for server
app = Flask(__name__)

# Create list for database to contain patient data
db = []


def init_server():
    """Initializes server conditions

    This function initializes the server log and can be used for any other
    tasks that you would like to run upon initial server start-up.  For
    example, it currently adds two patients to the database so that there is
    content in the database for testing.  Also, in the future, when an external
    database is utilized, the connection to that external database can be
    established here.

    Note:  As currently written, this function does not need a unit test as
    it does not do any data manipulation itself.
    """
    add_patient_to_db("Ann Ables", 101, "A+")
    add_patient_to_db("Bob Boyles", 202, "B-")
    logging.basicConfig(filename="health_db_server.log", level=logging.DEBUG,
                        filemode='w')


@app.route("/new_patient", methods=["POST"])
def new_patient_handler():
    """Handles requests to the /new_patient route for adding a new patient to
    server database

    The /new_patient route is a POST request that should receive a JSON-encoded
    string with the following format:

    {"name": str, "id": int, "blood_type": str}

    The function then calls a driver function that implements the functionality
    of this route and receives an "answer" and "status_code" from this
    driver function.  Finally, it returns the "answer" using jsonify and the
    status_code.

    Note: This function only does the three things that a flask handler should
    do.  1. Get data from the request. 2. Call other functions to do the
    work. 3. Return the results.  Therefore, it does not need a unit test.

    Returns:
        str, int: message including patient data if successfully added to the
                  database or error message if not, followed by a status code
    """
    # Get the data from the request
    in_data = request.get_json()
    # Call OTHER function to Do the request
    answer, status_code = new_patient_driver(in_data)
    # Provide a response
    return jsonify(answer), status_code


def new_patient_driver(in_data):
    """Implements /new_patient route for adding a new patient to server
    database

    The flask handler function for the /new_patient route calls this function
    to implement the functionality.  It receives as a parameter a dictionary
    that should contain the needed information in the following format:

    {"name": str, "id": int, "blood_type": str}

    The function first calls a validation function to ensure that the needed
    keys and data types exist in the dictionary, then calls a function to
    add the patient data to the database.  The function then returns to the
    caller either a status code of 200 and the patient info if it was
    successfully added, or a status code of 400 and an error message if there
    was a validation problem.

    Args:
        in_data (any type): the input data received by the route.  Ideally,
        it is a dictionary.

    Returns:
        str, int: message including patient data if successfully added to the
                  database or error message if not, followed by a status code
    """

    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    answer, status_code = validate_server_input(in_data, expected_keys,
                                                expected_types)
    if status_code != 200:
        return answer, status_code
    add_patient_to_db(in_data["name"], in_data["id"], in_data["blood_type"])
    print(db)
    return True, 200


def validate_server_input(in_data, expected_keys, expected_types):
    """Validates that input data to server contains a dictionary with the
    correct keys and data types

    Various routes for this server are POST requests that receive JSON-encoded
    strings which should contain dictionaries.  To avoid server errors, this
    function checks that the input data is a dictionary, that it has the
    specified keys, and specified data types.

    Args:
        in_data (any type): the input data that has been deserialized from a
            JSON string.  Ideally, it is a dictionary.
        expected_keys (list): a list of the needed keys in the input dictionary
        expected_types(list): a list of the types for each value in the
            dictionary, in the same order as their corresponding key in
            expected_keys

    Returns:
        str or bool , int: returns True, 200 if data validation is successful.
            Returns an error message string and 400 if data validation is
            unsuccessful.
    """
    if type(in_data) is not dict:
        return "The input was not a dictionary.", 400
    for key, expected_type in zip(expected_keys, expected_types):
        if key not in in_data:
            error_message = "Key {} is missing".format(key)
            return error_message, 400
        if type(in_data[key]) is not expected_type:
            error_message = "Value of key {} is not of type {}"\
                .format(key, expected_type)
            return error_message, 400
    return True, 200


def add_patient_to_db(patient_name, id_no, blood_type):
    """Creates new patient database entry

    This function receives information about the patient, creates a new
    dictionary containing the patient information, and appends the diction to
    the database list.

    The dictionary for each patient will have the following format:
        {"name": <name_string>,
         "id": <id_int>,
         "blood_type": <string>,
         "tests": <dictionary>}
    The "tests" dictionary will look like this:
        {"test_name1": [test_result1, test_result2, etc.],
         "test_name2": [test_result3, test_result4, etc.],
         etc. }

    Args:
        patient_name (str): name of patient
        id_no (int):  patient id number, usually a medical record number
        blood_type (str):  patient blood type, ex. "AB+"

    Returns:
        bool: True indicating that the patient was successfully saved to the
            database
    """

    new_patient = {"name": patient_name, "id": id_no,
                   "blood_type": blood_type, "tests": {}}
    db.append(new_patient)
    return True


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_results_handler(patient_id):
    """ GET route to obtain database entry for a patient by id number

    This function implements a GET route with a variable URL.  The desired
    patient id number is included as part of the URL.  The function calls
    another function to implement the functionality and receives an
    answer and status code from that function, which it then returns.

    Args:
        patient_id (str): the patient id taken from the variable URL

    Returns:
        str, int: An error message if patient_id was invalid or a results
        string containing the patient data, plus a status code.
    """
    answer, status_code = get_results_driver(patient_id)
    return answer, status_code


def get_results_driver(patient_id):
    """ Implements the /get_results route to obtain database entry for a
    patient by id number

    This function implements the /get_results route.  The desired patient id
    number, which was part of the variable URL, is sent to this function as
    an argument.  The function then calls a validation function to ensure that
    the given id is an integer.  If the validation passes, the function calls
    another function to retrieve the test results for that patient id.  The
    answer and status code from that function are returned.

    Args:
        patient_id (str): the patient id taken from the variable URL

    Returns:
        str, int: An error message if patient_id was invalid or a results
        string containing the patient data, plus a status code.
    """
    answer, status_code = validate_convert_patient_id(patient_id)
    if status_code != 200:
        return answer, status_code
    answer, status_code = get_patient_tests_from_database(answer)
    return answer, status_code


def validate_convert_patient_id(patient_id):
    """Convert the patient id is an integer if possible

    The patient_id, received as a string, is checked to see if it contains an
    integer.  If it does, the string is converted to an integer and is returned
    with a status code of 200.  If the string does not an integer, an error
    message is returned with a status code of 400.

    Args:
        patient_id (str): the patient id string taken from the variable URL

    Returns:
        int or string, int: the patient id as an integer or an error
        message string; status code
    """
    try:
        patient_id_int = int(patient_id)
    except ValueError:
        return "Patient_id was not an integer", 400
    return patient_id_int, 200


def get_patient_tests_from_database(patient_id):
    """Retrieves test results for a patient from the database

    The database list of dictionaries is searched for the dictionary with
    the correct patient_id in the "id" key-value pair.  When found, the
    "test" value is returned with a 200 status code.  If the patient id is not
    found, an error message string and a 400 status code are returned

    Args:
        patient_id (int): the patient id to find in the database

    Returns:
        dict or string, int: A dictionary of test results if the patient id is
        found, otherwise an error string; status code
    """

    for patient in db:
        if patient["id"] == int(patient_id):
            return patient["tests"], 200
    return "Patient_id {} was not found".format(patient_id), 400


@app.route("/add_test", methods=["POST"])
def add_test_handler():
    """Implements /add_test route for adding a new test result to a patient
    record in the server database

    The /add_test route is a POST request that should receive a JSON-encoded
    string with the following format:

    {"id": int, "test_name": str, "test_result": int}

    The function then calls a driver function that implements the test
    addition.  The result and status code from that driver function are then
    returned.

    Returns:
        str, int: message saying test data successfully added to the
                  database or error message if not, followed by a status code
    """

    in_data = request.get_json()
    answer, status_code = add_test_driver(in_data)
    return jsonify(answer), status_code


def add_test_driver(in_data):
    """Adds a new test result to a patient record in the server database

    This function implements the functionality of the /add_test route.  The
    input parameter should be a dictionary with the following format:

    {"id": int, "test_name": str, "test_result": int}

    The function first calls a validation function to ensure that the needed
    keys and data types exist in the dictionary.  If that validation passes,
    another function is then called to find and add the test results to the
    patient record.  The second function returns a status code of 200 and a
    success message, or a status code of 400 and an error message if the
    patient id did not exist.

    Returns:
        str, int: message saying test data successfully added to the
                  database or error message if not, followed by a status code
    """
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    answer, status_code = validate_server_input(in_data, expected_keys,
                                                expected_types)
    if status_code != 200:
        return answer, status_code
    answer, status_code = add_test_to_patient(in_data)
    print(db)
    return answer, status_code


def add_test_to_patient(in_data):
    """ Finds the specified patient and adds a new test result to the patient
    record

    The function calls another function that finds the specified patient and
    returns the "tests" dictionary for that patient if the patient exists.
    If the patient does not exist, a status code of 400 is returned and this
    function returns the error message and status code.  If the patient did
    exist, the function checks to see if the test_name already exists as a key
    in the "tests" dictionary.  If so, it appends the sent test_result to the
    list associated with the key.  If not, a new key is created using the test
    name and a new list with the single result is created.  The function then
    return a success message and a status code of 200.

    Args:
        in_data (dict): contains the patient id, the name of the test to add,
            and the test result.

    Returns:
        str, int: a success or error message, status code
    """
    tests, status_code = get_patient_tests_from_database(in_data["id"])
    if status_code == 400:
        return tests, status_code
    test_name = in_data["test_name"]
    if test_name in tests:
        tests["test_name"].append(in_data["test_result"])
    else:
        tests["test_name"] = [in_data["test_result"]]
    return "Test added", 200


if __name__ == "__main__":
    init_server()
    app.run()
