import requests

server = "http://127.0.0.1:5000"


def upload_patient_data_to_server(patient_name, patient_id, patient_bloodtype):
    new_patient = {"name": patient_name, "id": patient_id,
                   "blood_type": patient_bloodtype}
    r = requests.post(server + "/new_patient", json=new_patient)
    return r.text

# r = requests.get(server+"/get_results/333")
# print(r.status_code)
# print(r.text)
#
# new_test = {"id": 333, "test_name": "HDL", "test_result": 51}
# r = requests.post(server+"/add_test", json=new_test)
# print(r.status_code)
# print(r.text)
#
# new_test = {"id": 333, "test_name": "LDL", "test_result": 40}
# r = requests.post(server+"/add_test", json=new_test)
# print(r.status_code)
# print(r.text)
#
# new_test = {"id": 333, "test_name": "HDL", "test_result": 52}
# r = requests.post(server+"/add_test", json=new_test)
# print(r.status_code)
# print(r.text)
#
# r = requests.get(server+"/get_results/333")
# print(r.status_code)
# print(r.text)
