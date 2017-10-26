import  wx
import  Config
from    Bitmap  import Bitmap
from    Cell    import Cell


class Display(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, Config.TITLE)

        self.bitmapPxWidth      = Config.NB_COLS * Config.SPRITE_SIZE
        self.bitmapPxHeight     = Config.NB_ROWS * Config.SPRITE_SIZE
        #self.panel              = wx.Panel(self)
        # Bitmap holder to draw the board on
        self.shownBoardBitmap       = Bitmap(self, wx.ID_ANY)
        # Bitmap to draw on and render to the shown bitmap
        self.drawableBoardBitmap    = wx.EmptyBitmap(self.bitmapPxWidth, self.bitmapPxHeight)

        self.shownBoardBitmap.SetBitmap(self.drawableBoardBitmap)

        # main window's scaling for it's internal components
        self.verticalSizer = wx.BoxSizer(wx.VERTICAL)
        self.doGuiLayout()

        self.bindEvents()
        self.CenterOnScreen()
        self.SetFocus()
        self.Show()

    # Fit everything visually
    def doGuiLayout(self):
        self.verticalSizer.Add(self.shownBoardBitmap, 1, wx.EXPAND | wx.ALL)
        self.SetSizerAndFit(self.verticalSizer)

    def bindEvents(self):
        self.Bind(wx.EVT_LEFT_DOWN, self.onBoardClicked)

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

    def convertCoordinatesFromPxToCell(self, pxPos):
          return int(pxPos / Config.SPRITE_SIZE)

    def onBoardClicked(self, evt):
        clickedCellX = self.convertCoordinatesFromPxToCell(evt.X)
        clickedCellY = self.convertCoordinatesFromPxToCell(evt.Y)

        print("Board clicked (x%d y%d), cell (x%d y%d)" % (
            evt.X
          , evt.Y
          , clickedCellX
          , clickedCellY
        ))

    def onDummyCallback(self, *_):
        print("Dummy callback")

# !class Display
