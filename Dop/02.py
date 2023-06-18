def ridge_case(name):
    result = ""
    index = 0
    for char in name:
        if index % 2 == 0: 
            result += char.upper()
        else:
            result += char.lower()
        index += 1  
    return result   

name1 = "doctor" 
nick1 = ridge_case(name1)
nick2 = ridge_case("city")
nick3 = ridge_case("manty")

print(nick1)
print(nick2)
print(nick3)