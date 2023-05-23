number = 56789
last_digit = number % 10
number = number // 10 #деление без остатка
new_number = last_digit * 10000 + number
print(new_number)
