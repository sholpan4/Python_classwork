def ridge_case(name):
    result = ""
    size = len(name)
    
    for i in range(size):
        if i % 2 == 0: 
            result += name[i].upper()
        else:
            result += name[i].lower() 
    return result   

name1 = "doctor" 
nick1 = ridge_case(name1)
print(nick1)
