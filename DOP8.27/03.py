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