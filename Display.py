import  wx
import  Config
from    Cell    import Cell


class Display(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, Config.TITLE)

        self.bitmapPxWidth      = Config.NB_COLS * Config.SPRITE_SIZE
        self.bitmapPxHeight     = Config.NB_ROWS * Config.SPRITE_SIZE

        # Bitmap holder to draw the board on
        self.shownBoardBitmap   = wx.StaticBitmap(self, wx.ID_ANY)
        # Bitmap to draw on and render to the shown bitmap
        self.drawableBoardBitmap = wx.EmptyBitmap(self.bitmapPxWidth, self.bitmapPxHeight)

        self.shownBoardBitmap.SetBitmap(self.drawableBoardBitmap)

        # main window's scaling for it's internal components
        self.verticalSizer = wx.BoxSizer(wx.VERTICAL)
        self.doGuiLayout()

        self.Show()

    # Fit everything visually
    def doGuiLayout(self):
        self.verticalSizer.Add(self.shownBoardBitmap, 1, wx.EXPAND | wx.ALL)
        self.SetSizerAndFit(self.verticalSizer)

    def drawBoard(self, board):
        for row in board.getMatrix():
            for cell in row:
                self.drawCell(cell)
        # Forces redrawing
        self.shownBoardBitmap.SetBitmap(self.drawableBoardBitmap)

    def drawCell(self, cell):
        dc = wx.MemoryDC()
        dc.SelectObject(self.drawableBoardBitmap)
        dc.DrawBitmap(
            wx.Bitmap(cell.getCurrentStatusSpritePath())
            , cell.getXPos() * Config.SPRITE_SIZE
            , cell.getYPos() * Config.SPRITE_SIZE
        )
        dc.SelectObject(wx.NullBitmap)

# !class Display


if __name__ == "__main__":
    app = wx.App()
    display = Display()
    app.MainLoop()