#предикат = True or False

my_numbers = [1, 4, -23, 356, 0, -4556, 234]

def true_or_false(num):
    if num > 0:
        return True
    else:
        return False

my_list = map(true_or_false, my_numbers)
print(list(my_list))