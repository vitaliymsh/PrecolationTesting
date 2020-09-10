import quantumrandom
import numpy as np


class SquareMatrix:


    def __init__(self, size):
        self.create_matrix(size)


    def get_value(self, coordinate):
        return self.matrix[coordinate[0]][coordinate[1]]


    def set_value(self, value, coordinate):
        self.matrix[coordinate[0]][coordinate[1]] = value


    def get_coordinate_free(self):
        while True:
            x = int(int(quantumrandom.randint(0, self.size)))
            y = int(int(quantumrandom.randint(0, self.size)))
            print("{} - {}; {} - {}".format(x, type(x), y, type(y)))
            if self.get_value((x, y)) == 0:
                return (x, y)


    def create_matrix(self, size):
        self.matrix = np.zeros(shape=(size, size))
        self.size = size


    def get_matrix(self):
        return self.matrix
  

    def print_matrix(self):
        for i in self.matrix:
            print(i)


matrix = SquareMatrix(3)
while True:
    matrix.set_value(1, matrix.get_coordinate_free())
    matrix.print_matrix()
    input()

class PrecolationCheck:

    matrix = None

    def __init__(self):
        self.main()

    def dfs(self, matrix):
        pass


    def setup(self):
        self.matrix = Matrix(3)


    def main(self):
        self.setup()
        while True:
            coordinate = self.matrix.get_coordinate_free()
            if coordinate[1] == 0:
            



