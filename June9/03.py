print("Solve: 2 + 2 * 2")
num = int(input("Enter the result:"))

while num != 6:
    print("Wrong!")
    num = int(input("Try again:"))
    if num == 6:
        break
print("Right! 6")