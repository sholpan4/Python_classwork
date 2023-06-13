

for r in range(8):
    print(r+1, end=" ")
    for c in range(8):
        if (r + c) %2 == 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()
