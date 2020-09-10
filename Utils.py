from enum import Enum

class Color():
    staticColorList = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "GOLD"]
    subColor = ["CORAL1", "STEELBLUE1", "PALE GREEN", "KHAKI", "ORCHID3", "GRAY29", "LIGHT GOLDENROD"]


class MoveList(Enum):
    LEFT = [0, -1]
    RIGHT = [0, 1]
    UP = [-1, 0]
    DOWN = [1, 0]

    