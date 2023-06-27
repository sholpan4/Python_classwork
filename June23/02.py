first_list = [1, 2, 3, 4, 5]
second_list = [6, 7, 8, 9]

first_list.append(6)
print(first_list)

first_list.extend(second_list)
print(first_list)

first_list.insert(0, "cake")
print(first_list)

#######################

third_list = [1, 2, 5, True, "cake"]  #True будет считать как 1 и False = 0
element_removed = third_list.remove("cake")
print(third_list, element_removed)

element_popped = third_list.pop(3)
print(third_list, element_popped)

third_list.clear()
print(third_list)

######################

forth_list = ["cake", "cake", "cake", "future"]
i = forth_list.index("future")
print(i)

a = forth_list.count("cake")
print(a)

fifth_list = ["cake", "moon", "pencil", "future"]
fifth_list.sort(reverse=False)
print(fifth_list)

######################
sixth_list = ["Hello", 666, 0, "sun", [6, 7, 8]]
sixth_list.reverse()
print(sixth_list)

seventh_list = sixth_list.copy()
# sixth_list = seventh_list
seventh_list[2] = "welcome"
seventh_list[0][2] = "A"

print(sixth_list)
print(seventh_list)

print(seventh_list is sixth_list)
