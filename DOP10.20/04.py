class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
 
    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

 
    @property
    def size(self):
        rows = len(self.matrix)
        cols = 0
        for row in self.matrix:
            if len(row) > cols:
                cols = len(row)
 
        return (rows, cols)

import random
 
matrix = [[i for i in range(random.randrange(0, 9))] for i in range(random.randrange(0, 9))]
inst = Matrix(matrix)
print(inst)
print(inst.size)