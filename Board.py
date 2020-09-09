import Case
import random

class Board : 

    #__size
    #__boardMatrix
    #__nbOfColor

    #constructor ---------------
    def __init__(self, size, nbOfColor): 
        self.__size = size
        self.__boardMatrix = self.init_boardMatrix(self.__size)
        self.__nbOfColor = nbOfColor


    #methods -------------------
    def init_boardMatrix(self, size): #initialize matrix
        matrix = []
        for j in range (size) :
            line = []
            for i in range (size):
                line.append(Case.Case(False, None))
            matrix.append(line)
        return matrix

        
    def init_EndCases(self): #define the Cases that are marked as End
        
        for i in range(self.__nbOfColor):
            for j in range (2):
                randX, randY = random.randint(0, self.__size - 1), random.randint(0, self.__size - 1)
                while self.__boardMatrix[randX][randY].getEnd():
                    randX, randY = random.randint(0, self.__size - 1), random.randint(0, self.__size - 1)
                self.__boardMatrix[randX][randY].setEnd(True)
              
    
    #utility
    def show_boardMatrix(self):   #display state of the game
        for i in range (self.__size) : 
            for j in range (self.__size) : 
                print(self.__boardMatrix[i][j].getEnd(), end=" ")
            print()
    
    def getBoard(self):
        return self.__boardMatrix
                


    

    
    
        