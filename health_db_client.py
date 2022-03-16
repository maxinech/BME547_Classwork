import requests


server = "http://127.0.0.1:5000"

# new_patient = {"name": "Chris", "id": "m", "blood_type": "O+"}
# r = requests.post(server + "/add_patient", json=new_patient)
# print(r.status_code)
# print(r.text)

r = requests.get(server + "/get_results/uh")
print(r.status_code)
print(r.text)
