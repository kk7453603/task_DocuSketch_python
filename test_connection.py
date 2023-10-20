import requests

res = requests.get("http://127.0.0.1:8080/api/keyvalue/1")
print(res.text)

res = requests.post("http://127.0.0.1:8080/api/keyvalue",json={"key":12,"value":"da"})
print(res.status_code)

req = requests.put("http://127.0.0.1:8080//api/keyvalue/1",json={"value":13})
print(req.status_code)
