#быстрая сотрировка

user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list =list(map(lambda x: int(x), user_in))

def quick_sort(the_list):
    if len(the_list) <= 1:
        return the_list
    pivot = the_list[0]
    less_list = list(filter(lambda x: x < pivot, the_list))  # [x for x in the_list if x < pivot]
    equal_list = list(filter(lambda x: x == pivot, the_list))
    more_list = list(filter(lambda x: x > pivot, the_list))
    result = quick_sort(less_list) + equal_list + quick_sort(more_list)
    return result

print(quick_sort(my_list))