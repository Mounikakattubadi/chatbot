import requests

res = requests.post("http://localhost:5000/chat", json={"message":"how are you?"})
print(res.json())
