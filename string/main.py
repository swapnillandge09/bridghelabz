import json

# # Load JSON data from a file:
# with open("example.json","r") as file:
#     data = json.load(file)

# print(json.dumps(data , indent=4))

# print("Company Name",data['company']['name'])
# print("Founded Year",data['company']['founded'])

# for empl in data['company']['employees']:
#      print(f"Employee ID: {empl['id']}")
#      print(f"Name:{empl['name']}")
#      print(f'Position:{empl['position']}')
#      print(f"Skills:{empl['skills']}")

##add

# with open("sample.json","r") as file:
#     data = json.load(file)

# data["hobbies"] = ['Travlling'],['playing']

# with open("sample.json","w") as file:
#     json.dump(data , file , indent=4)

## delete
# with open("sample.json",'r') as file:
#     data = json.load(file)
# del data["hobbies"]
# with open("sample.json","w") as file:
#     json.dump(data,file,indent=4)

# with open("sample.json","r") as file:
#     data = json.load(file)

# data['fullname'] = data.pop('name')

# with open("sample.json","w") as file:
#     json.dump(data,file,indent=4)

with open("sample.json","r") as file:
    data = json.load(file)
data['name'] = data.pop('fullname')
with open("sample.json",'w') as file:
    json.dump(data,file,indent=4)