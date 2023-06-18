def ridge_case(name):
    result = ""
    index = 0
    for char in name:
        if char == " ":
            index += 1

        if index % 2 == 0: 
            result += char.upper()
        else:
            result += char.lower()
        index += 1  
    return result   

name1 = "Илон Маск" 
nick1 = ridge_case(name1)

print(nick1)

