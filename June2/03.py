def factor (num):
    if num == 1:
        return 1
    return num * factor(num-1)  #result will be bring back on the wayback
    #return factor(num+1) * num #need exact math calc

result = factor(6)
print(result)