class Matrix:
    def __init__(self, matrix_string):
        self.newList = matrix_string.split('\n')
        print(self.newList)
    def row(self, index):
        testList = []
        testRow = self.newList[index-1].split(' ')
        for number in testRow:
            testList.append(int(number))
        return testList
    def column(self, index):
        gridLen = len(self.newList)
        testList = []
        for row in range(gridLen):
            testList.append(int(self.newList[row].split(' ')[index-1]))
        return testList
matrix = Matrix("9 8 7\n5 3 2\n6 6 7")
# print row at index
print(matrix.row(1))
# print column at index
print(matrix.column(1))