user_in = input("Введите числа через запятую:")
user_list = user_in.split(",")

# numbers = []
#
# for x in user_list:
#     numbers.append(int(x))
#
# print(user_list)
# print(numbers)


def get_last_digit(num):
    return num % 10  # на 2 вернет сначала нечетные

print(user_list)
try:
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
except ValueError:
    message = "Нужны только числа, и только через запятую!"
else:
    end_list = sorted(user_list, key=get_last_digit, reverse=True) #key для передачи функции скобки убрать
    another_list = [str(x) for x in end_list]
    message = " - ".join(another_list)
print(message)