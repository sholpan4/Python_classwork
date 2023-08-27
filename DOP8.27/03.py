import json

try:
    fp = open('inp.json')
except FileNotFoundError:
    print('File not found')
    exit()
    
info = json.load(fp)
fp.close()
result = {}

for soldier in info['soldiers']:
    print(soldier['height'])
    height = soldier['height']
    for size, value in info['sizes'].items():
        print(size, value)
        if value['from'] < height <= value['to']:
            if size in result:
                result[size] += 1
            else:
                result[size] = 1
                
print(result)
      
out = open('out.json', 'w')
json.dump(result, out)
out.close()  


print(info['soldiers'][3]['height'])
print(info['soldiers'][5]['first_name'], info['soldiers'][5]['last_name'], info['soldiers'][5]['height'])

size_list = []
for value in info['sizes'].values():
    size_list.append(str(value['to']))   

print(size_list)
a = " ".join(size_list)    
print(a)

str(item['to'])

b_list = map(lambda x: x in , info['sizes'].values())
print(" ".join(b_list))