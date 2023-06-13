
num = 1

if num < 10:
    print("Less")
else: #можно не писать
    print("More or equal")

while num < 10: #повторяет пока условие не поменяют можно увеличить к 10ке or  T/F 1/0
    #print("Less,", num) #ждать команды от пользователя
    num += 1 #to end ctrl+c or 
    if num == 5:
        continue #не идет дальше, пропускает остальное #break
    print("Less,", num)
else: #можно не писать
    print("More or equal")

print("The end")