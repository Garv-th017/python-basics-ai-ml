# JSON is used to Deal with the send ad receieve data 
# python has the built in JSON module we can use 

import json

# to convert from the Json to the python we use 


data = '{"name": "Garv", "age": 22}'

result = json.loads(data)

print(result)
print(type(result))