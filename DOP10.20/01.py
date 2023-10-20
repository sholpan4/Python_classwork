import sys

print(sys.argv)

#`--text filename.txt --debuglevel warning --mode delayed --output stdout`

def get_list(my_list):
    my_dict = {}
    for i in range(1, len(my_list)-1):
        if my_list[i] == '--text':
            my_dict[my_list[i].lstrip('-')] = my_list[i+1]
        elif my_list[i] == '--debuglevel':
            my_dict[my_list[i].lstrip('-')] = my_list[i+1]
        elif my_list[i] == '--mode':
            my_dict[my_list[i].lstrip('-')] = my_list[i+1]
        elif my_list[i] == '--output':
            my_dict[my_list[i].lstrip('-')] = my_list[i+1]
       
    return my_dict 

print(get_list(sys.argv))







    # my_dict = {my_list[i]: my_list[i+1] for i in range (1, len(my_list), 3)} 

    # it = iter(my_list)
    # my_dict = dict(zip(it, it))