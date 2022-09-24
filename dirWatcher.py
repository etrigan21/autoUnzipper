import os
from unzipper import checkForZipAndUnzip
import time
import json

start = True
oldList = []
def watcherFunction(ongoing):
    print("start")
    while True:
        path = (json.loads(open("autopen.config", "r").read())["watchDir"])
        if ongoing.value == True and (json.loads(open("autopen.config", "r").read())["status"]) == "alive":
            global oldList
            global start
            x = os.listdir(path)
            if x != oldList and not start:
                diff = list(set(x) - set(oldList))
                checkForZipAndUnzip(diff)
            oldList = x
            start = False
            time.sleep(0.5)
        elif (json.loads(open("autopen.config", "r").read())["status"]) == "dead":
            break