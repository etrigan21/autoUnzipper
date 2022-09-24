import json
def modifyConfig(path):
    f = open("autopen.config","r")
    strVal = f.read()
    x=  json.loads(strVal)
    x["watchDir"] = path
    f.close()
    z = open("autopen.config", "w")
    z.write(json.dumps(x))
    z.close()

def modifyAliveStatus(value):
    f = open("autopen.config","r")
    strVal = f.read()
    x=  json.loads(strVal)
    x["status"] = value
    print(x)
    f.close()
    z = open("autopen.config", "w")
    z.write(json.dumps(x))
    z.close()