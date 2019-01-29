import json

dataDict={}
with open("emp.json") as jsonData:
   dataFetch = jsonData.read()
   config = json.loads(dataFetch)
for k in config:
   dataDict["name"]=k["name"]
   dataDict["age"]=k["age"]
   dataDict["salary"]=k["salary"]
for k,v in dataDict.items():
  print(v)
