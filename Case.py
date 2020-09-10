class Case : #a Case with a color, End inherit from Case

    """
    color : string / int
    """

    #constructor
    def __init__(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color