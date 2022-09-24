import json
f = open("autopen.config","r")
strVal = f.read()
x=  json.loads(strVal)
print(x)