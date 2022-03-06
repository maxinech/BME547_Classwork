import requests


server = "http://127.0.0.1:5000"
# r = requests.get("http://127.0.0.1:5000/")
# print(r.status_code)
# print(r.text)
#
# r = requests.get("http://127.0.0.1:5000/info")
# print(r.status_code)
# print(r.text)

# out_data = {"name": "David", "hdl_result": 65}
#
# r = requests.post(server + "/hdl_check", json=out_data)
# print(r.status_code)
# print(r.text)

out_data = {"a": 3, "b": 5}
r = requests.post(server + "/add", json=out_data)
print(r.status_code)
print(r.text)
a = r.json()
print(a[0])

r = requests.get(server + "/add/3/5")
