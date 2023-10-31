import random

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


my_table = Table(5)
print(my_table)