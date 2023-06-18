def get_sequence(text, symbol):
    result = ""   
    for x in text:
        if x == symbol:           
            result += symbol
        elif result:
                break                 
    return result

a = get_sequence("coommmmao", "o")
print(a)