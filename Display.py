import  wx
import  Config
import  Event
from    Bitmap  import Bitmap
from    Cell    import Cell


class Display(wx.Frame):

    def __init__(self, game):
        wx.Frame.__init__(self, None, wx.ID_ANY, Config.TITLE)

        self.game = game

        self.bitmapPxWidth      = Config.NB_COLS * Config.SPRITE_SIZE
        self.bitmapPxHeight     = Config.NB_ROWS * Config.SPRITE_SIZE
        #self.panel              = wx.Panel(self)
        # Bitmap holder to draw the board on
        self.shownBoardBitmap       = Bitmap(self, wx.ID_ANY)
        # Bitmap to draw on and render to the shown bitmap
        self.drawableBoardBitmap    = wx.EmptyBitmap(self.bitmapPxWidth, self.bitmapPxHeight)
        self.shownBoardBitmap.SetBitmap(self.drawableBoardBitmap)

        self.textPlayerTurn = wx.StaticText(self, label="White player", style=wx.BORDER_NONE)
        self.textTurnNumber = wx.StaticText(self, label="Turn #0")
        self.buttonPass     = wx.Button(self, label="Pass")
        self.buttonGiveUp   = wx.Button(self, label="Give up")

        # main window's scaling for it's internal components
        self.horizontalSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.verticalSidePanelSizer = wx.BoxSizer(wx.VERTICAL)
        self.doGuiLayout()

        self.menu = wx.MenuBar()
        self.menuFile = wx.Menu()
        self.menuFileNewGame = self.menuFile.Append(wx.ID_ADD , "New Game", "Restarts the game")
        self.menuFileExit    = self.menuFile.Append(wx.ID_EXIT, "Quit"    , "Exit this program")
        self.menu.Append(self.menuFile, "&File")
        self.SetMenuBar(self.menu)

        self.bindEvents()

        self.CenterOnScreen()
        self.SetFocus()
        self.Show()


    # Fit everything visually
    def doGuiLayout(self):

        # Layout for the player and turn textBoxes
        self.verticalSidePanelSizer.Add(self.textPlayerTurn, 1, wx.CENTER | wx.ALL, 16)
        self.verticalSidePanelSizer.Add(wx.StaticLine(self), 0.1, wx.EXPAND | wx.ALL, 16)
        self.verticalSidePanelSizer.Add(self.textTurnNumber, 1, wx.CENTER | wx.ALL, 16)

        # Empty text field to add a blank space in the middle of the sidePanel
        self.verticalSidePanelSizer.Add(wx.StaticText(self), 3, wx.EXPAND)
        # This means the textBoxes will be aligned to the top,
        # and the buttons "pass" & "give up" at the bottom

        # Buttons layout
        self.verticalSidePanelSizer.Add(self.buttonPass  , 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 16)
        self.verticalSidePanelSizer.Add(self.buttonGiveUp, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 16)

        # Overall layout of the window
        # Board drawn on the left side
        self.horizontalSizer.Add(self.shownBoardBitmap      , 3, wx.EXPAND | wx.ALL, 32)
        # Side panel drawn on the right side
        self.horizontalSizer.Add(self.verticalSidePanelSizer, 1, wx.EXPAND | wx.ALL)
        # Apply the layout
        self.SetSizerAndFit(self.horizontalSizer)


    def bindEvents(self):
        # mouse clicks on the bitmap
        self.Bind(wx.EVT_LEFT_DOWN, self.onBoardClicked, self.shownBoardBitmap)
        # Side panel buttons
        self.Bind(wx.EVT_BUTTON, self.onPassClicked  , self.buttonPass)
        self.Bind(wx.EVT_BUTTON, self.onGiveUpClicked, self.buttonGiveUp)
        # menu bindings
        self.Bind(wx.EVT_MENU, self.onExitMenu   , self.menuFileExit)
        self.Bind(wx.EVT_MENU, self.onNewGameMenu, self.menuFileNewGame)


    def onNewGameMenu(self, *_):
        print("onNewGameMenu()")
        confirmNewGameDialog = wx.MessageDialog(
            self
            , "Start a new game ?"
            , "Restart"
            , wx.OK | wx.CANCEL | wx.ICON_NONE
        )
        userAnswer = confirmNewGameDialog.ShowModal()
        confirmNewGameDialog.Destroy()
        if userAnswer == wx.ID_OK:
            print("User restarting the game ...")
            raise NotImplementedError


    def onExitMenu(self, *_):
        confirmExitDialog = wx.MessageDialog(
            self
            , "Do you really want to exit the game ?"
            , "Exit"
            , wx.OK | wx.CANCEL | wx.ICON_NONE
        )
        userAnswer = confirmExitDialog.ShowModal()
        confirmExitDialog.Destroy()
        if userAnswer == wx.ID_OK:
            self.Destroy()


    def onPassClicked(self, *args):
        print("onPassClicked()")
        wx.PostEvent(self.game, Event.EvtPlayerPass())

    def onGiveUpClicked(self, *args):
        print("onGiveUpClicked()")
        raise NotImplementedError

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
        wx.PostEvent(self.game, Event.EvtPlayerPlay(position=wx.Point(clickedCellX, clickedCellY)))

    def onDummyCallback(self, *_):
        print("Dummy callback")

# !class Display
