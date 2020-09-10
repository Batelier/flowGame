import Case
import random
import Utils
import End

class Board :
    """
    __size : int
    __boardMatrix : [[]]
    __nbOfColor : int
    __currentPos : [int, int]
    """

    #constructor ---------------
    def __init__(self, size, nbOfColor): 
        self.__size = size
        self.__boardMatrix = self.init_boardMatrix(self.__size)
        self.__nbOfColor = nbOfColor
        self.__listOfEnd = [] #containing all extremities
        self.__currentPos = []

    #methods -------------------
    def init_boardMatrix(self, size): #initialize matrix
        matrix = []
        for j in range (size) :
            line = []
            for i in range (size):
                line.append(Case.Case(None))
            matrix.append(line)
        return matrix
        
    def init_EndCases(self): #define the Cases that are marked as End
        for i in range(self.__nbOfColor):
            for j in range (2):
                randX, randY = random.randint(0, self.__size - 1), random.randint(0, self.__size - 1)
                while type(self.__boardMatrix[randX][randY]) == End.End :
                    randX, randY = random.randint(0, self.__size - 1), random.randint(0, self.__size - 1)
                newEnd = End.End(Utils.Color.staticColorList[i])
                self.__boardMatrix[randX][randY] = newEnd
                self.__listOfEnd.append(newEnd)
                self.__currentPos = [randX, randY]
                #self.__boardMatrix[randX][randY].setColor()

    def deselectAllEnds(self):
        for i in self.__listOfEnd:
            i.setIsSelected(False)
        #for i in self.__listOfEnd:
        #    print(i.getIsSelected(), end = " ")

    #Movement logic ---------------------------------------
    def arrowKeyPressed(self, move): #check if can move, move, update current Case, update EndList
        potentialNextPos = [self.getCurrentPos()[0] + move[0], self.getCurrentPos()[1] + move[1]]
        if not self.checkIfPosPossible(potentialNextPos):
            return
        if not self.checkIfMovePossible(potentialNextPos):
            return 
        self.setCurrentPos(potentialNextPos)

    def checkIfPosPossible(self, pos): #check if we are trying to go on a Case that is in the Game or not
        for i in pos : 
            if i < 0 or i > (self.__size -1):
                print("impossible path : out of bound")
                return False
        return True
    
    def checkIfMovePossible(self, pos): #check if the rules of the game allow the move or not
        # +++ Check color of line or end to know f we can complete a line
        if not (self.__boardMatrix[pos[0]][pos[1]]).getColor() == None:
            print("impossible path : Case already occupied")
            return False
        return True

    #utility ------------------------------------------------
    def show_boardMatrix(self):   #display state of the game
        for i in range (self.__size) : 
            for j in range (self.__size) : 
                print(self.__boardMatrix[i][j].getColor(), end=" ")
                #print(type(self.__boardMatrix[i][j]), end = " ")
            print()
    
    def getBoard(self):
        return self.__boardMatrix

    def getCurrentPos(self): #return the position of the current selected case
        return self.__currentPos

    def setCurrentPos(self, currentPos):
        self.__currentPos = currentPos
        print("current pos : ", str(self.getCurrentPos()))