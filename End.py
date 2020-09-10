#A case that is an extremity, inherit from Case
import Case

class End(Case.Case):

    def __init__(self, color):
        super().__init__(color)
        line = "line"

        self.isSelected = False

    def setIsSelected(self, boolean): #set the selected End
        self.isSelected = boolean
    
    def getIsSelected(self):
        return self.isSelected 