import json
# https://www.programiz.com/python-programming/json
try:
    with open(r'./data.json','r') as f:
        j_object = json.load(f)
except ValueError as e:
    print(e)
    raise Exception
print(j_object)

with open(r'./data.json', 'w') as f:
    json.dump(j_object, f, indent = 4)