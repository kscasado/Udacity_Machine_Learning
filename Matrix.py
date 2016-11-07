class Matrix:
    ##creates a matrix with a 2d list for rows and colums and a
    ##tuple for the shape
    def __init__(mList,size):
        self.list = mList
        self.shape = size
    ##first uses isValid to check if you can multiply the matrix then
    ##if you can it uses the 2d list of both matrix and returns a new matrix
    ##with the result
    def multiply(matrix):
        if isValid(matrix):
            for i in range(matrix.shape[0]):
                for y in range (self.shape[1]):
                    for x in range(self.shape[0]):
                        newList[i][y]+= matrix.list[i][y] * self.list[x][y]
                        return Matrix(newList,(self.shape[0],matrix.shape[1]))
        else:
            print "not valid matrix"
    ##checks whether the matrix is valid
    def isValid(matrix):
        if self.shape[1]==matrix.shape[1]:
            return true
        else:
            return false
    ##goes through the list and multiplies it by a scalar
    def multiplyScalar(scalar):
        for x in range (self.shape[1]):
            for y in range(self.shape[0]):
                self.list[x][y]*=scalar
