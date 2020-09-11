#Flow Game
from tkinter import Tk, Label, Button
import BoardInterface
import Board
import Case

# 7 color maximum
size, nbOfColor = 10, 3

#back
board = Board.Board(size, nbOfColor)
board.init_EndCases()
board.show_boardMatrix()

#visual
boardInterface = BoardInterface.BoardInterface(size, board)
