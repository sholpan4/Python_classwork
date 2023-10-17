class Matrix:
    matrix = []
    c_row = 0
    c_cols = 0

    def __init__(self, row, cols):
        self.row = row
        self.cols = cols
        
        for r in range(row):
            for c in range(cols):
                self.matrix[r][c] = 0
        

    
    def set(self, row, cells):
        for x in cells:
            row.append(x) #set(1, [3,4,5])

    def __next__(self):
        pass

somelist = [4, 5, 6]    
a = Matrix(somelist)
print(a)