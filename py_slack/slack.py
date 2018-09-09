import requests

BASE_URL = 'https://hooks.slack.com/services'
API_PATH = '{YOUR_API_PATH}'
msg = 'Hello World'

data = '{{"text":"{}"}}'.format(msg)
url =  '{}/{}'.format(BASE_URL, API_PATH)

# print(data)
# print(url)

r = requests.post(url, data)
print(r.status_code)