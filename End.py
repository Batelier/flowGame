#A case that is an extremity, inherit from Case
import Case
import Utils

class End(Case.Case):

    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.__color = color
        self.__endMasterPos = pos
        self.__line = [pos] # pass
        self.isSelected = False

    def setIsSelected(self, boolean): #set the selected End
        self.isSelected = boolean
    
    def getIsSelected(self):
        return self.isSelected 
    
    def getEndMasterPos(self):
        return self.__endMasterPos

    def linkCase(self, case) : #Function that add a case to the line of this End
        self.__line.append(case.getPos())
        #case add this End as a master
        case.setEndMasterPos(self.__endMasterPos)      

    def getCurrentPosOfLine(self): #return pos of last case of the line
        return self.__line[-1]