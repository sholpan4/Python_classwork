user_in1 = input("Сколько денег у вас есть:")
user_in2 = input("Сколько стоит шоколад:")

try:
    num1 = int(user_in1)
    chocolate = int(user_in2)

except ValueError:
    message = "Вы ввели неправильные данные"

else:
    result1 = num1 // chocolate
    result2 = num1 - (result1 *chocolate)
    message = "Вы можете купить %d шоколадок" % result1 
    message2 = "и у вас останется %s денег" % result2

print(message, message2)