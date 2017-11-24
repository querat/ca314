import  wx
import  Event
from    Cell    import Cell
from    Display import Display
from    Board   import Board

class Game(wx.EvtHandler):

    class Player:
        WHITE   \
        , BLACK \
        = range(2)

    class Status:
        START \
        , WHITE_PLAYING \
        , BLACK_PLAYING \
        = range(3)

    def __init__(self):
        wx.EvtHandler.__init__(self)
        self.display = Display(self)
        self.board = Board()
        self.display.drawBoard(self.board)
        self.status = self.Status.BLACK_PLAYING
        self.doBindings()

    def doBindings(self):
        self.Bind(Event.EVT_PLAYER_PLAY, self.onPlay)
        self.Bind(Event.EVT_PLAYER_PASS, self.toggleTurn)
        pass

    def isOver(self):
        # TODO
        return False

    def updateDisplay(self):
        # TODO
        self.display.drawBoard(self.board)
        pass

    def determineWinner(self):
        # TODO
        return Game.Player.BLACK

    def onPlay(self, evt):
        if (self.isOver()):
            print("Game is over, you can't play a turn !")

        x, y = evt.position.x, evt.position.y
        print("onPlay(): click on cell %d:%d" % (x, y))

        colorOfNewToken = Cell.Color.BLACK
        if self.status == Game.Status.WHITE_PLAYING:
            colorOfNewToken = Cell.Color.WHITE

        # Invalid play
        if not self.board.addToken(x, y, colorOfNewToken):
            return

        # last possible move of the game has been played
        if self.board.isFull():
            print("onPlay(): board full")
        self.toggleTurn()
        self.updateDisplay()

    def toggleTurn(self, *_):
        if (self.status != Game.Status.BLACK_PLAYING and
            self.status != Game.Status.WHITE_PLAYING):
            print("Can't toggle turn: not playing")
            return False
        if self.status == self.Status.BLACK_PLAYING:
            self.status = self.Status.WHITE_PLAYING
        else:
            self.status = self.Status.BLACK_PLAYING
        return True

if __name__ == "__main__":
    app = wx.App()
    game = Game()
    app.MainLoop()