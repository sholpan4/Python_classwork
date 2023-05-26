user_in1 = input("Enter first number: ")
user_in2 = input("Enter second number: ")

template = """
Сумма чисел:        %.2f
Разность чисел:     %.2f
Произведение чисел: %.2f
Частность чисел:    %.2f
""" #будем задавать многострочную строку

try: 
    num1 = float(user_in1) #дробное число
    num2 = float(user_in2)
    num3 += 1
except ValueError as my_error:
    print(my_error) #выводит сообщение ошибки ValueError
    message = "Вы ввели неправильные данные"
except NameError:
    message = "нет такой переменной"
else:
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    message = template % (sum, sub, mul, div)

print(message)