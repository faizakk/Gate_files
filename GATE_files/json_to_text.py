import json


with open('4821.json') as json_data:
    d= json.load(json_data)



with open('data.txt', 'w') as outfile:
    json.dump(d, outfile, indent=4)
# print(d)
# json.dump(d,fp, indent=4)
