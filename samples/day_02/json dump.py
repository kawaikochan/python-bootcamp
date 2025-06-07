import json

data=[
    {'name':"alice","age":30,"work":"nurse"},
    {'name':"kai","age":10,"work":"student"},
]
with open("people.json","w")as file:
    json.dump(data,file)

with open("people.json","r")as file:
    data=json.load(file)

    print(data)

