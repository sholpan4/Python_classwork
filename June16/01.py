
def show_mul_table(n, i = 2):
    if i >= 10:
        return
    print(n * i)
    show_mul_table(n, i + 1)

def show_all_table(n=2):
    if n >=10:
        return
    show_mul_table(n)
    print()
    show_all_table(n+1)

