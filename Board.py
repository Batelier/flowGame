import Case
import random
import Utils
import End
import BoardInterface
import time
import sys

class Board :
    """
    __size : int
    __boardMatrix : [[]]
    __nbOfColor : int
    __currentPos : [int, int]
    """

    #constructor ---------------
    def __init__(self): 
        self.__size = None
        self.__boardMatrix = None
        self.__nbOfColor = None
        self.__listOfEnd = [] #containing all extremities
        self.__currentPos = []
        self.__currentEndPos = [] #current pos of the end master of the line 
        self.__boardCompleted = False

    #methods -------------------
    def init_RandomBoardMatrix(self, size, nbOfColor): #initialize matrix
        self.__nbOfColor = nbOfColor
        self.__size = size
        matrix = []
        for j in range (size) :
            line = []
            for i in range (size):
                line.append(Case.Case(None, [j, i]))
            matrix.append(line)
        self.__boardMatrix = matrix
        self.init_RandomEndCases()
        
    def init_RandomEndCases(self): #define the Cases that are marked as End
        for i in range(self.__nbOfColor):
            for j in range (2):
                randX, randY = random.randint(0, self.__size - 1), random.randint(0, self.__size - 1)
                while type(self.__boardMatrix[randX][randY]) == End.End :
                    randX, randY = random.randint(0, self.__size - 1), random.randint(0, self.__size - 1)
                newEnd = End.End(Utils.Color.staticColorList[i], [randX, randY])
                self.__boardMatrix[randX][randY] = newEnd
                self.__listOfEnd.append(newEnd)
        self.__currentEndPos = self.__listOfEnd[0].getPos()
        self.__currentPos = self.__listOfEnd[0].getPos()
    
    def init_boardMatrixFromFile(self, fileLocation): #import premade terrain from text file
        try:
            terrainFile = open(fileLocation, "r")
            txt = terrainFile.read()
            txt = txt + "\n"
            line = []
            matrix  =[]
            x, y = 0, 0
            for i in txt :
                if i == " ":
                    x += 1
                    continue
                elif i == "\n":
                    # for i in range(len(line)): print(line[i].getColor())
                    print(len(line))
                    matrix.append(line)
                    line = []
                    x = 0
                    y += 1
                    continue
                elif int(i) == 0:
                    line.append(Case.Case(None, [y, x]))
                else:
                    newEnd = End.End(Utils.Color.staticColorList[int(i) - 1], [y, x])
                    self.__listOfEnd.append(newEnd)
                    line.append(newEnd)
            # print("Matrix lenght : ", str(len(matrix)))
            self.__size = len(matrix[0])
            self.__boardMatrix = matrix
            self.__currentEndPos = self.__listOfEnd[0].getPos()
            self.__currentPos = self.__listOfEnd[0].getPos()

        except :
            print("An error occured while reading the file")
        

    def deselectAllEnds(self):
        for i in self.__listOfEnd:
            i.setIsSelected(False)

    #Movement logic ---------------------------------------
    def arrowKeyPressed(self, move): #check if can move, move, update current Case, update EndList
        if self.__boardCompleted : return
        print("INFO : ", str(self.getCurrentPos()))
        try:
            nextPos = [self.getCurrentPos()[0] + move[0], self.getCurrentPos()[1] + move[1]]
            if not self.checkIfPosPossible(nextPos): #check if out of bound
                return
            #if self.checkIfLineCompleted(nextPos):
            #    pass
            self.checkIfLineCompleted(nextPos)
            if not self.checkIfMovePossible(nextPos): #check if occupied by another color
                return 

            self.setCurrentPos(nextPos)

            print("Current End pos : ", str(self.__currentEndPos))
            currentCase = self.__boardMatrix[nextPos[0]][nextPos[1]]
            currentMaster = self.__boardMatrix[self.__currentEndPos[0]][self.__currentEndPos[1]]

            #link current master to the current case
            currentMaster.linkCase(currentCase)

            #set New Color
            newColor = self.getAttenuateColorOf(currentMaster.getColor())
            currentCase.setColor(newColor)
            self.update_buttonColor(currentCase.getPos(), newColor)
            #BoardInterface.BoardInterface.update_buttonColor(currentCase.getPos(), newColor)
            #self.show_boardMatrix()
        except :
            print("An error occured, please select an end")

        
    def update_buttonColor(self, position, color): #à mettre en command avec les flèches
        BoardInterface.BoardInterface.btnMatrix[position[0]][position[1]].configure(bg = color)

    def getAttenuateColorOf(self, string): #Get the subcolor of an end
        return Utils.Color.subColor[Utils.Color.staticColorList.index(string)]

    def checkIfPosPossible(self, pos): #check if we are trying to go on a Case that is in the Game or not
        for i in pos : 
            if i < 0 or i > (self.__size -1):
                print("impossible path : out of bound")
                return False
        return True
    
    def checkIfMovePossible(self, pos): #check if the rules of the game allow the move or not
        if not (self.__boardMatrix[pos[0]][pos[1]]).getColor() == None:
            #print("impossible path : Case already occupied")
            return False
        return True
    
    def checkIfLineCompleted(self, pos): #return True if current line is finished
        currentCase = self.__boardMatrix[self.__currentPos[0]][self.__currentPos[1]]
        currentEnd = self.__boardMatrix[self.__currentEndPos[0]][self.__currentEndPos[1]]
        nextCase = self.__boardMatrix[pos[0]][pos[1]]
        nextCaseEnd = None
        try:
            nextCaseEnd = self.__boardMatrix[nextCase.getEndMasterPos()[0]][nextCase.getEndMasterPos()[1]]
        except:
            return False
        
        #if we find the other End Case to finish the line
        print("POS comparison : ", str(nextCase.getEndMasterPos()), " current End : ", str(currentEnd.getPos()))
        if (nextCaseEnd.getColor() == currentEnd.getColor() and nextCase.getEndMasterPos() != currentEnd.getPos()):
            print(str(nextCaseEnd.getColor()), " LINE COMPLETED")

            #removing completed End
            i = 0
            while (i < len(self.__listOfEnd)):
                if self.__listOfEnd[i].getColor() == nextCaseEnd.getColor():
                    self.update_buttonColor(self.__listOfEnd[i].getPos(), Utils.Color.victoryColor)
                    self.__listOfEnd.pop(i)
                    i -= 1
                i += 1

            #attributing new current End
            try:
                self.__currentEndPos = self.__listOfEnd[0].getPos()
                self.__currentPos = self.__listOfEnd[0].getPos()
            except :
                print("THE GAME IS FINISHED")
                self.__boardCompleted = True
                self.endAnimation(self.checkIfVictory())                

    def checkIfVictory(self): #check if every case of the game have a color attributed
        for line in self.__boardMatrix:
            for case in line:
                if case.getColor() == None:
                    return False
        return True
    
    def endAnimation(self, boolean):
        color = Utils.Color.lostColor
        endText = Utils.Text.lostText
        if boolean:
            color = Utils.Color.victoryColor
            endText = Utils.Text.victoryText
        for i in range(self.__size):
            for j in range(self.__size):
                self.update_buttonColor([i,j], color)
                self.update_victoryText([i, j])
            #time.sleep(.01)
        print(endText)
    
    def update_victoryText(self, position): #à mettre en command avec les flèches
        BoardInterface.BoardInterface.btnMatrix[position[0]][position[1]]['text'] == 'Victory'
    
    #utility ------------------------------------------------
    def show_boardMatrix(self):   #display state of the game
        for i in range (self.__size) : 
            for j in range (self.__size) : 
                print(self.__boardMatrix[i][j].getColor(), end=" ")
                #print(type(self.__boardMatrix[i][j]), end = " ")
            print()

    def printListOfEnd(self):
        print("LIST OF END : ")
        for i in range(len(self.__listOfEnd)):
            print(self.__listOfEnd[i].getColor()) 
        print("END LIST OF END")

    #getter setter ---------------------
    def getBoard(self):
        return self.__boardMatrix

    def getCurrentPos(self): #return the position of the current selected case
        return self.__currentPos

    def setCurrentPos(self, currentPos):
        self.__currentPos = currentPos
        print("current pos : ", str(self.getCurrentPos()))
    
    def setCurrentEndPos(self, pos): #pos of the selected End
        self.__currentEndPos = pos

    def getListOfEnd(self):
        return self.__listOfEnd

    def isBoardCompleted(self):
        return self.__boardCompleted