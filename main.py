#Flow Game
from tkinter import Tk, Label, Button
import BoardInterface
import Board
import Case
import sys

#For random terrain creation : 
randomTerrainGeneration = False
size, nbOfColor = 5, 2 # 7 color maximum

#Importing a terrain from a text file :
terrainImportation = True
fileLocation = "premade_terrain/terrain1.txt"

#back
board = Board.Board()
if randomTerrainGeneration : 
    board.init_RandomBoardMatrix(size, nbOfColor)
elif terrainImportation : 
    board.init_boardMatrixFromFile(fileLocation)
else : 
    print("No terrain generation chosen, quiting")
    sys.exit()

board.show_boardMatrix()

#visual
boardInterface = BoardInterface.BoardInterface(size, board)
