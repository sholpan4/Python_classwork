import random
import sys

class Table:
    # table = []
    def __init__(self, size):
        self.size = size
        self.table = []
        for r in range(size):
            self.table.append([])
            for c in range(size):
                self.table[r].append(random.randint(1, 10))
    
    def __repr__(self):
        result = ""
        for r in range(self.size):
            result += "\n"
            for c in range(self.size):
                result += str(self.table[r][c]) + " "
        return result

        # s = ''
        # for r in self.table:
        #     s += str(r) + "\n"
        # return s[:-1]


houses = Table(5)
route = list(sys.argv[1:])
# route = list(map(int,sys.argv[1:]))
# size = max(route)+1
# houses = Table(size)
# print("houses", houses, sep='')
# text = str(my_table) #если нужно вернуть строку
print(route)

result = 0
for i in range(len(route)-1):
    row = route[i]
    col = route[i+1]
    result += houses.table[row][col]
print(result)