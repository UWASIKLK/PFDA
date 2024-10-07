# playing with json

import json
data = {
    'Name': 'Joe',
    'Age':21,
    'Student': True
}
jsonString = json.dumps(data)
print(data)
print(jsonString)