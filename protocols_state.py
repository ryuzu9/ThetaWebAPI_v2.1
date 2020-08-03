#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests

cmdURL = "http://192.168.1.1/osc/state"
res = requests.post(cmdURL)
json_dict = json.loads(res.text)

# Takes a unique value
print("Takes a unique value : " + json_dict["fingerprint"])

# State of the camera
print("State of the camera :")
print("    Battery level : " + str(json_dict["state"]["batteryLevel"]))
print("    Storage URI : " + str(json_dict["state"]["storageUri"]))
print("    Continuous shooting state : " + str(json_dict["state"]["_captureStatus"]))
print("    Shooting time of movie (sec) : " + str(json_dict["state"]["_recordedTime"]))
print("    Remaining time of movie (sec) : " + str(json_dict["state"]["_recordableTime"]))
# Only for RICOH THETA S firmware v01.82 or later / RICOH THETA Z1 or later
# print("    Elapsed time for interval composite shooting (sec) : " + str(json_dict["state"]["_compositeShootingElapsedTime"]))
print("    URL of the last saved file : " + str(json_dict["state"]["_latestFileUrl"]))
print("    Charging state : " + str(json_dict["state"]["_batteryState"]))
print("    API version currently set : " + str(json_dict["state"]["_apiVersion"]))
print("    Plugin running state : " + str(json_dict["state"]["_pluginRunning"]))
print("    Plugin web server state : " + str(json_dict["state"]["_pluginWebServer"]))
# Only for RICOH THETA Z1 or later
# print("    Shooting function status : " + str(json_dict["state"]["_function"]))
# Only for RICOH THETA Z1 or later
# print("    My setting changed state : " + str(json_dict["state"]["_mySettingChanged"]))
print("    Error information of the camera : " + str(json_dict["state"]["_cameraError"]))

# Error information of the camera
NumberOfElements = len(json_dict["state"]["_cameraError"])
print("Error information of the camera :")
for i in range(NumberOfElements):
    print(json_dict["state"]["_cameraError"][i])