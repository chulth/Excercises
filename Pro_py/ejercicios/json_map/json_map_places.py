import json
import os
# base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base)
# input_file = json.load(open(base + "/department.json"))
input_file=json.load(open('Pro_py/ejercicios/json_map/fixture/places.json', 'r'))
output_file=open('Pro_py/ejercicios/json_map/fixture/departments.json', 'w')

departments=[]
for item in input_file:
    department={}
    department['name']=item.get('provincia').get('nombre')
    department['id']=item.get('provincia').get('id')
    if department not in departments:
        departments.append(department)
        print(department)
output_file.write(json.dumps(departments))
output_file.close()
print(len(departments))