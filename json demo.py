import json


json_file = open("MOCK_DATA.json")
json_data = json.load(json_file)
#print(json_data)


class Student:
    def __init__(self,id,name,image,gender):
        self.id = id
        self.name = name
        self.image = image
        self.gender = gender

for i in json_data:
    student = Student(i["id"],i["name"],i["image"],i["gender"])