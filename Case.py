class Case : #a Case with a color and an endMaster, End inherit from Case

    """
    color : string
    endMasterPos : [x, y] The position of the end that begins the line
    pos : [int, int] : position of the case
    """

    #constructor
    def __init__(self, color, pos):
        self.__color = color
        self.__endMasterPos = None
        self.__position = pos

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getEndMasterPos(self):
        return self.__endMasterPos

    def setEndMasterPos(self, pos):
        self.__endMasterPos = pos
    
    def getPos(self):
        return self.__position
