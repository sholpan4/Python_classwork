user_in1 = input("Введите ростояние в кв между городами:")
user_in2 = input("За сколько часов хотите добраться?:")

try:
    km = int(user_in1)
    hours = int(user_in2)

except ValueError:
    message = "Вы ввели неправильные данные"

else:
    speed = km / hours
    message = "Вам нужно ехать со скоростью %s км/ч" % speed

print(message)