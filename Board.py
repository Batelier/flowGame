import Case

class Board : 

    #__size
    #__boardMatrix

    #constructor ---------------
    def __init__(self, size): 
        self.__size = size
        self.__boardMatrix = self.init_boardMatrix(self.__size)


    #methods -------------------
    def init_boardMatrix(self, size): #initialize matrix
        lines = [Case.Case(False, None)] * size #later replace 0 by a Case Object
        return [lines] * size

    
    #utility
    def show_boardMatrix(self):   #display state of the game
        for i in range (self.__size) : 
            for j in range (self.__size) : 
                print(self.__boardMatrix[i][j].getColor(), end=" ")
            print()
                


    

    
    
        