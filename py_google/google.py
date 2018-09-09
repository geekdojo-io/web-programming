import requests

r = requests.get('http://www.google.com')
print(r.text)
print(r.status_code)