import requests

# Δοκιμή SQL Injection
url = "http://localhost:5000/login"
data = {"username": "admin' OR '1'='1", "password": "anything"}
response = requests.post(url, data=data)

if "Login successful!" in response.text:
    print("SQL Injection vulnerability detected!")
    exit(1)
else:
    print("No SQL Injection vulnerability detected.")
    exit(0)
