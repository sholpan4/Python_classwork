#польз. вводит никнэйм, преобазуем в "НиКнНэЙм"

name = input("Enter name:")
#print(name.upper())
result = ""
index = 0

for char in name:
    if index % 2 == 0: 
        result += char.upper()
    else:
        result += char.lower()
    index += 1     

print(result)