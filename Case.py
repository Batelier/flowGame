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

