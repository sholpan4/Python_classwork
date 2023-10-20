
class Matrix:
    matrix = []
    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        for r in range(rows):
            self.matrix.append([])
            for c in range(cols): 
                self.matrix[r].append(4)


    def __repr__(self)->str:
        result = ""
        for r in range(self.rows):
            result += "\n"
            for c in range(self.cols): 
                result += str(self.matrix[r][c]) + " "
        return result

    def __add__(self, other):
        other = Matrix(self.rows, self.cols)
        numbers =[]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    other.append(numbers)
                    numbers = []
        return Matrix(other)


my_table = Matrix(4, 6)

second_table = Matrix(2, 3)

third_table = my_table = second_table

print(my_table)