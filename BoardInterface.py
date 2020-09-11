from tkinter import *
import Board
import End
import Utils

class BoardInterface: #Graphical interface view & interactions

    """ variables
    board : Board
    frame : Frame
    btnMatrix : [][] containing all buttons of the game
    size : int
    """
    btnMatrix = []

    def __init__(self, size, board):
        self.size = size
        self.board = board
        root = Tk()
        root.geometry("500x500")
        self.frame=Frame(root)

        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        self.frame.grid(row=0, column=0, sticky=N+S+E+W)
        grid=Frame(self.frame)
        grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
        Grid.rowconfigure(self.frame, 7, weight=1)
        Grid.columnconfigure(self.frame, 0, weight=1)

        #self.btnMatrix = [] #
        for x in range(size):
            btnLine = []
            for y in range(size):
                btn = Button(self.frame, bg=board.getBoard()[x][y].getColor())
                btn.grid(column=y, row=x, sticky=N+S+E+W)
                btnLine.append(btn)
            self.btnMatrix.append(btnLine)
                
        for x in range(size):
            Grid.columnconfigure(self.frame, x, weight=1)
        for y in range(size):
            Grid.rowconfigure(self.frame, y, weight=1)

        #---Key Binding
        root.bind("<Button-1>", self.btnCommand)
        root.bind("<Left>", self.leftKeyPressed)
        root.bind("<Right>", self.rightKeyPressed)
        root.bind("<Up>", self.upKeyPressed)
        root.bind("<Down>", self.downKeyPressed)
        root.mainloop()
        #self.update_buttonColor([1, 1], "black")

    #Mouse & KeyBoard interactions : -----------------------------
    def leftKeyPressed(self, event):
        print("left key pressed")
        self.board.arrowKeyPressed(Utils.MoveList.LEFT.value)

    def rightKeyPressed(self, event):
        print("right key pressed")
        self.board.arrowKeyPressed(Utils.MoveList.RIGHT.value)

    def upKeyPressed(self, event):
        print("up key pressed")
        self.board.arrowKeyPressed(Utils.MoveList.UP.value)

    def downKeyPressed(self, event):
        print("down key pressed")
        self.board.arrowKeyPressed(Utils.MoveList.DOWN.value)

    @staticmethod
    def update_buttonColor(self, position, color): #à mettre en command avec les flèches
        self.btnMatrix[position[1]][position[0]].configure(bg = color)

    def btnCommand(self, event): #Used to select an End, set The current Pos Case
        x = event.x_root - self.frame.winfo_rootx()
        y = event.y_root - self.frame.winfo_rooty()
    
        z = self.frame.grid_location(x, y)
        print("Case clicked : ", str(self.board.getBoard()[z[1]][z[0]].getPos()), " master is : ", 
            str(self.board.getBoard()[z[1]][z[0]].getEndMasterPos()))
        #if master is completed, return

        if (type(self.board.getBoard()[z[1]][z[0]]) == End.End):
            if self.board.getListOfEnd().__contains__(self.board.getBoard()[z[1]][z[0]]):
                self.board.deselectAllEnds()
                self.board.getBoard()[z[1]][z[0]].setIsSelected(True)
                self.board.setCurrentPos(self.board.getBoard()[z[1]][z[0]].getCurrentPosOfLine())
                self.board.setCurrentEndPos([z[1], z[0]])

    