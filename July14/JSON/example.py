import json

data = '{"type": "forecast", "duration": 3, "city": "Karaganda", "country_code": "kz"}'
#обязательно " " для json data
request = json.loads(data)
request['city'] = "Almaty"

data = json.dumps(request) #data = json.dumps(request, ensure_ascii=False)
print(data)