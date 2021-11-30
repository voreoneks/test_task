import json
import sys

tests_file = sys.argv[1]
values_file = sys.argv[2]

with open(tests_file, 'r') as json_file:
    tests = json.load(json_file)

with open(values_file, 'r') as json_file:
    values = json.load(json_file)

values_dict = {}

for k_values, v_values in values.items():
    for item in v_values:
        values_dict[item['id']] = item['value']

def search(data):
    for item in data:
        if 'value' in item.keys():
            item['value'] = values_dict.get(item['id'])
        if item.get('values'):
            search(item['values'])

for k, v in tests.items():
    search(v)

with open('report.json', 'w') as json_file:
    json.dump(tests, json_file, indent = 2)