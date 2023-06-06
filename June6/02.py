def is_simple(num, div = 2):
    if num < 2:
        return False
    if div >= num: #div>=num num == div
        return True
    if num % div == 0:
        return False
    else:
        return is_simple(num, div+1)
    
print(9.5, is_simple(9.5))  #print(is_simple(9.5))
print(12, is_simple(12))