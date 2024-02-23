endpoint = 'YOUR_ENDPOINT' #Replace with your endpoint
key = 'YOUR_KEY' #Replace with your key
import urllib.request
import json
import os
data =  {
  "Inputs": {
    "input1": [
      {
        "CulmenLength": 46.6,
        "CulmenDepth": 17.8,
        "FlipperLength": 193,
        "BodyMass": 3800
      }
    ]
  },
  "GlobalParameters": {}
}

body = str.encode(json.dumps(data))
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ key)}
req = urllib.request.Request(endpoint, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    json_result= json.loads(result)
    output = json_result["Results"]["WebServiceOutput0"][0]
    print('Cluster: {}'.format(output["Assignments"]))
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))
    # Print the headers to help debug
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
