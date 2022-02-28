import requests

r = requests.get(
    "http://api.github.com/repos/dward2/ClassworkSpring2022/branches")

print(r)
print(type(r))
print("Status code = {}".format(r.status_code))
print("Text = {}".format(r.text))

if r.status_code != 200:
    print("There was a problem")
    print(r.text)
    exit()

answer = r.json()

for branch in answer:
    print(branch["name"])


print("done")
