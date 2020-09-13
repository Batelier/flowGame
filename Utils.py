from enum import Enum

class Color():
    staticColorList = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "CYAN2", None]
    subColor = ["CORAL1", "STEELBLUE1", "PALE GREEN", "KHAKI", "ORCHID3", "GRAY29", "CYAN3"]
    victoryColor = "GOLD"
    lostColor = "BLACK"

class MoveList(Enum):
    LEFT = [0, -1]
    RIGHT = [0, 1]
    UP = [-1, 0]
    DOWN = [1, 0]

class Text():
    victoryText = "Victory !"
    lostText = "Defeat .. Every case must have a color .."

    