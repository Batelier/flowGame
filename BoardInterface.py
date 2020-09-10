from tkinter import *
import Board

class BoardInterface:

    def __init__(self, size, board):
        root = Tk()
        root.geometry("500x500")
        frame=Frame(root)

        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        frame.grid(row=0, column=0, sticky=N+S+E+W)
        grid=Frame(frame)
        grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
        Grid.rowconfigure(frame, 7, weight=1)
        Grid.columnconfigure(frame, 0, weight=1)

        #example values
        for x in range(size):
            for y in range(size):
                btn = Button(frame, bg=board.getBoard()[x][y].getColor())
                btn.grid(column=x, row=y, sticky=N+S+E+W)

        for x in range(size):
            Grid.columnconfigure(frame, x, weight=1)

        for y in range(size):
            Grid.rowconfigure(frame, y, weight=1)

        self.init_boardInterface(board)
        root.mainloop()

    def init_boardInterface(self, board):
        print("yomek")