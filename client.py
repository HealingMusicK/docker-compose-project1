import requests 
URL = 'http://localhost:5000' 
response = requests.get(URL) 
print(response.status_code)
print("status code : ", response.status_code)