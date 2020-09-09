class Board : 

    #__size
    #__boardMatrix

    #constructor ---------------
    def __init__(self, size): 
        self.__size = size
        self.__boardMatrix = self.init_boardMatrix(self.__size)


    #methods -------------------
    def init_boardMatrix(self, size): #initialize matrix
        lines = [0] * size #later replace 0 by a Case Object
        return [lines] * size

    

    #utility
    def show_boardMatrix(self):   #display state of the game
        for lines in self.__boardMatrix:
            print(lines)


    

    
    
        