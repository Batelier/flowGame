from enum import Enum

class Color():
    staticColorList = ["RED", "BLUE", "GREEN", "YELLOW"]

class MoveList(Enum):
    LEFT : [0, -1]
    RIGHT : [0, 1]
    UP : [-1, 0]
    DOWN : [1, 0]

    