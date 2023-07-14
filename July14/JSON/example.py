import json

# data = '{"type": "forecast", "duration": 3, "city": "Karaganda", "country_code": "kz"}'
# #обязательно " " для json data
# request = json.loads(data) #словарь = загружаем строку
# request['city'] = "Almaty"
#
# data = json.dumps(request) #data = json.dumps(request, ensure_ascii=False)
# print(data)

with open("example.txt", encoding="utf-8") as myfile:  #python closes file self
    request = json.load(myfile)

request['city'] = "Almaty"

with open("example.txt", "w", encoding="utf-8") as myfile:
     json.dump(request, myfile)

print(request['city'])