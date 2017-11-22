import wx
from Display import Display
from Board import Board

class Game:

    def __init__(self):
        self.display = Display()
        self.board = Board()
        self.display.drawBoard(self.board)



if __name__ == "__main__":
    app = wx.App()
    game = Game()
    app.MainLoop()