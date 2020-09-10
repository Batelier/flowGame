from tkinter import *
import Board
import End

class BoardInterface:

    def __init__(self, size, board):
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

        #example values
        self.btnMatrix = []
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

        root.bind("<Button-1>", self.btnCommand)
        root.mainloop()
        #self.update_buttonColor([1, 1], "black")

    def update_buttonColor(self, position, color): #à mettre en command avec les flèches
        self.btnMatrix[position[1]][position[0]].configure(bg = color)

    def btnCommand(self, event):
        x = event.x_root - self.frame.winfo_rootx()
        y = event.y_root - self.frame.winfo_rooty()
    
        z = self.frame.grid_location(x, y) 
        print(type(self.board.getBoard()[z[1]][z[0]]))
        print(z)