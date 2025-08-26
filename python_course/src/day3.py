import os,time
import requests

BASE = "https://httpbin.org"

# response = requests.get(
#     f"{BASE}/user-agent",
#     timeout=5
#     )
# response.raise_for_status()
# Status = response.status_code
# content = response.headers["content-type"]
# data = response.json()
# print(data)
# print(response.json)
# print(response.json()["user-agent"])
########################################
# response1 = requests.post(
#     f"{BASE}/response-headers",
#     #params={'freeform': 'test'},
#     timeout=5
# )
# response1.raise_for_status
# content = response1.headers['content-type']
# data = response1.json()
# print(data)
#######################################
with requests.session() as session:
    for i in range(3):
        r = session.get(f"{BASE}/user-agent", timeout=5)
        x = session.get(f"{BASE}/ip")
        if r.status_code ==  200 and x.status_code == 200:
            break

print(r.status_code)
print(r.json())
print(x.json())
