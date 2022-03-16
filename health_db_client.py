import requests


server = "http://127.0.0.1:5000"

new_patient = {"name": "Chris", "id": 333, "blood_type": "O+"}
r = requests.post(server + "/add_patient", json=new_patient)
print(r.status_code)
print(r.text)

r = requests.get(server + "/get_results/333")
print(r.status_code)
print(r.text)

new_test = {"id": 333, "test_name": "HDL", "test_result": 51}
r = requests.post(server + "/add_test", json=new_test)
print(r.status_code)
print(r.text)

new_test = {"id": 333, "test_name": "LDL", "test_result": 40}
r = requests.post(server + "/add_test", json=new_test)
print(r.status_code)
print(r.text)

new_test = {"id": 333, "test_name": "HDL", "test_result": 52}
r = requests.post(server + "/add_test", json=new_test)
print(r.status_code)
print(r.text)

r = requests.get(server + "/get_results/333")
print(r.status_code)
print(r.text)
