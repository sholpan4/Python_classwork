user_in = input("Enter the cost of purchase:")
cost = int(user_in)

if cost < 1000:
    print("No discount")
elif cost < 2000:
    print("Discount 2%")
elif cost < 5000:
    print("Discount 5%")
else:
    print("Discount 10%")
print("END")
#если просто if будут дальнейшие сопоставления, все выполнятся, потому что они отдельные функции