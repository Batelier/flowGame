#Flow Game
from tkinter import Tk, Label, Button
import BoardInterface
import Board
import Case

size, nbOfColor = 5, 3

#back
board = Board.Board(size, nbOfColor)
board.init_EndCases()
board.show_boardMatrix()

#visual
boardInterface = BoardInterface.BoardInterface(size, board)
