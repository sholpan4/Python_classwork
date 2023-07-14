import json

data = '{"type": "forecast", "duration": 3, "city": "Karaganda", "country_code": "kz"}'

request = json.loads(data)

print(request["city"])