user_in = input(" Введите список чисел через запятую:")
user_list = user_in.split(",")
num = [int(x) for x in user_list]
num2 = []
for e in num:

    if e % 2 == 0:
        even_num = e * 2
        num2.append(even_num)
    else:
        odd_num = e - 3
        num2.append(odd_num)

print(num2)