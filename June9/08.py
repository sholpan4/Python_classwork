num = int(input("Enter the number:"))

for i in  range(2, num): 
    if num % i == 0:
        print("%d is not primer number!" % num)
        break
else:
    print("This is primer number!")
    