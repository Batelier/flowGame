#Flow Game
from tkinter import Tk, Label, Button
import BoardInterface
import Board
import Case

#For random terrain creation : 
randomTerrainGeneration = True
size, nbOfColor = 5, 2 # 7 color maximum

#back
board = Board.Board()
if randomTerrainGeneration : 
    board.init_boardMatrix(size, nbOfColor)
board.show_boardMatrix()

#visual
boardInterface = BoardInterface.BoardInterface(size, board)
