import requests
url = "https://my-awesome-site.com/wp-login.php"
username = "user"
password = "password"

Log_and_Pass = {'log': username, 'pwd': password}
response = requests.post(url, data={'log': username, 'pwd': password})
with open('1.html', 'w') as f:
    f.write(response.content)

if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
print('Status:', response.status_code, 'Headers:', response.headers, 'Response:',
      response.json())
