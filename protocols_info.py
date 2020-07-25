import requests
import json

cmdURL = "http://192.168.1.1/osc/info"
res = requests.get(cmdURL)
json_dict = json.loads(res.text)

# manufacturer
print("manufacturer : " + json_dict["manufacturer"])

# endpoints
print("endpoints :")
print("    httpPort : " + str(json_dict["endpoints"]["httpPort"]))
print("    httpUpdatesPort : " + str(json_dict["endpoints"]["httpUpdatesPort"]))

# api
NumberOfElements = len(json_dict["api"])
print("api :")
for i in range(NumberOfElements):
    print(json_dict["api"][i])