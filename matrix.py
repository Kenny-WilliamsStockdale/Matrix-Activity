class Matrix:
    def __init___(self, matrix_string="1 2\n 3 4"):
        self.newArray = matrix_string.split('\n').split("")
        return self.newArray
    def row(self, index):
        return self.newArray[index]

    def column(self, index):
        pass
