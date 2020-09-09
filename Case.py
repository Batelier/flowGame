class Case :

    """
    isAnEnd : bool
    color : string / int
    isLinked : bool #if the end is linked to another end
    """

    #constructor
    def __init__(self, isAnEnd, color):
        self.__isAnEnd = isAnEnd
        self.__color = color
        self.__isLinked = False #by default not linked

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getEnd(self):
        return self.__isAnEnd
    
    def setEnd(self, isEnd):
        self.__isAnEnd = isEnd
    
    

