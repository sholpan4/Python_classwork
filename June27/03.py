import random

list1 = []
num1 = random.randint(-100, 100)
num2 = random.randint(-100, 100)
if num1 > num2:
    num1, num2 = num2, num1

for x in range(10):
    num = random.randint(num1, num2)
    list1.append(num)

print(num1)
print(num2)
print(list1)