import requests
import time
url = "http://203.250.148.52:20516/Mobius/Embedded_contest/Sector_one"

while True:
  payload = "{\n    \"m2m:cin\": {\n        \"con\": \""+str(time.time())+"\"\n    }\n}"
  headers = {
    'Accept': 'application/json',
    'X-M2M-RI': '12345',
    'X-M2M-Origin': '{{aei}}',
    'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
  time.sleep(1)