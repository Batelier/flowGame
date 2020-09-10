class Case :

    """
    isAnEnd : bool
    color : string / int
    isLinked : bool #if the end is linked to another end
    """

    #constructor
    def __init__(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color