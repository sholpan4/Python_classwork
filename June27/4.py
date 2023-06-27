list1 = [4, 5454, 75, 87, 90, 200, 26363457557, 0]
counter = 1
counter_list = []
for i in range(len(list1)-1):
    if list1[i] <= list1[i+1]:
        counter += 1
    else:
        counter_list.append(counter)
        counter = 1
        a = max(counter_list)
print("MAX - ", a)