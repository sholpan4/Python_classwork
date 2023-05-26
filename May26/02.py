user_in1 = input("Который час:")
user_in2 = input("Сколько минут:")
user_in3 = input("Сколько секунд:")
seconds_total = 24 * 60 * 60

try: 
    hours = int(user_in1)
    minutes = int(user_in2)
    seconds = int(user_in3)
except ValueError:
    message = "Вы ввели не числа"
else:
    seconds_passed = hours * 60 * 60 + minutes * 60 + seconds
    seconds_left = seconds_total - seconds_passed
    message = "Осталось %s секунд" % seconds_left

print(message)