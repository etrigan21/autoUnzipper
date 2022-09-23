import os
from unzipper import checkForZipAndUnzip

start = True
oldList = []
def watcherFunction(path):
    global oldList
    global start
    x = os.listdir(path)
    if x != oldList and not start:
        diff = list(set(x) - set(oldList))
        checkForZipAndUnzip(diff)
    oldList = x
    start = False