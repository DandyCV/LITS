import json

j = '{"text" : "text", "number" : 1.2, "None" : null, "bool" : true}'

s = '[{"1": 1}, {"2": [2,2,2]}]'

print(json.loads(j))
print(json.loads(s)[1]["2"])

to_json = {"1":1, "2":2}

print(json.dumps(to_json))