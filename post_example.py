import requests

# out_data = {
#     "name": "Maxine",
#     "net_id": "jc895",
#     "e-mail": "jc895@duke.edu",
# }
# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
# print(r.text)
#
# r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
# print(r.text)


# message = {
#     "user": "Maxine",
#     "message": "Hi",
# }
# r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
#                   json=message)
# print(r.text)
#
# r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Sophie")
# print(r.text)


r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/jc895")
print(r.text)

bt1 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M1")
print(bt1.text)

bt2 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F5")
print(bt2.text)

bloodmatch = {
    "Name": "jc895",
    "Match": "Yes",
}

r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                  json=bloodmatch)
print(r.text)
