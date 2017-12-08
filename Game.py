import  wx
import  Event
from    Cell    import Cell
from    Display import Display
from    Board   import Board

class Game(wx.EvtHandler):

    class Player:
          WHITE \
        , BLACK \
        = range(2)


    def __init__(self):
        wx.EvtHandler.__init__(self)
        self.display        = Display(self)
        self.board          = Board()
        self.playerTurn     = self.Player.BLACK
        self.turnsNumber    = 1
        self.ConsecutiveTurnsPassed    = 0
        self.gameEnded      = False
        self.display.drawBoard(self.board)
        self.doBindings()


    def doBindings(self):
        self.Bind(Event.EVT_PLAYER_PLAY         , self.onPlay)
        self.Bind(Event.EVT_PLAYER_PASS         , self.onPass)
        self.Bind(Event.EVT_PLAYER_GIVEUP       , self.onPlayerGiveUp)
        self.Bind(Event.EVT_NEW_GAME_REQUESTED  , self.onNewGameRequested)


    def onNewGameRequested(self, *_):
        self.board          = Board()
        self.turnsNumber    = 1
        self.ConsecutiveTurnsPassed    = 0
        self.gameEnded      = False
        self.playerTurn = Game.Player.BLACK
        self.display.drawBoard(self.board)
        self.display.setTurnNumber(self.turnsNumber)
        self.display.setPlayerTurnText("Black player's turn")


    def updateDisplay(self):
        self.display.drawBoard(self.board)
        stringToDisplay = "%s player's turn"
        if self.playerTurn == self.Player.BLACK:
            stringToDisplay %= ("Black",)
        else:
            stringToDisplay %= ("White",)
        self.display.setPlayerTurnText(stringToDisplay)


    def determineWinner(self):
        # TODO
        return Game.Player.BLACK


    def onGameEnding(self, gaveUp=False):
        winner = self.determineWinner()
        self.gameEnded = True
        # TODO self.display.showPopup(blah)


    # Special ending condition: one player gives up
    def onPlayerGiveUp(self, *_):
        if self.gameEnded:
            notificationString = "You can't give up: the game already ended !"
            print(notificationString)
            self.display.showPopup(notificationString)
            return

        winner = "black"
        loser  = "white"
        if self.playerTurn == Game.Player.BLACK:
            winner = "white"
            loser  = "black"

        notificationString = "Game has ended: %s player gave up !" % (loser.capitalize(),)
        print(notificationString)
        self.gameEnded = True
        self.display.showPopup(notificationString)


    def onPass(self, *_):

        if self.gameEnded:
            errString = "Can't pass, game ended !"
            print(errString)
            self.display.showPopup(errString)
            return

        self.ConsecutiveTurnsPassed += 1
        self.switchPlayerTurn()

        # 2 turns passed in a row -> end the game
        if self.ConsecutiveTurnsPassed < 2:
            return
        msg = "Game is ending: both players passed in a row !"
        score = self.board.calculScore()
        msg += "\nWhite player's score : " + str(score[0])
        msg += "\nBlack player's score : " + str(score[1])
        if score[0] > score[1]:
            msg += "\nWhite player win the game!"
        elif score[0] < score[1]:
            msg += "\nBlack player win the game!"
        else:
            msg += "\nEquality!"
        print(msg)
        self.display.showPopup(msg)
        self.onGameEnding()


    def onPlay(self, evt):
        if (self.gameEnded):
            errString = "Game is over, you can't play a turn !"
            print("Game is over, you can't play a turn !")
            self.display.showPopup(errString)
            return

        x, y = evt.position.x, evt.position.y
        print("onPlay(): click on cell %d:%d" % (x, y))

        colorOfNewToken = Cell.Color.BLACK
        if self.playerTurn == Game.Player.WHITE:
            colorOfNewToken = Cell.Color.WHITE

        # Invalid play
        if not self.board.addToken(x, y, colorOfNewToken):
            return

        # player didn't pass -> reset the counter
        self.ConsecutiveTurnsPassed = 0

        # last possible move of the game has been played
        if self.board.isFull():
            print("onPlay(): board full")
            self.onGameEnding()

        self.board.removeCapturedTokens()
        self.toggleTurn()
        self.updateDisplay()


    def toggleTurn(self, *_):
        if (self.playerTurn != Game.Player.BLACK and
            self.playerTurn != Game.Player.WHITE):
            print("Can't toggle turn: not playing")
            return False
        self.switchPlayerTurn()
        self.incrementTurnNumber()
        return True


    def switchPlayerTurn(self):
        if self.playerTurn == self.Player.BLACK:
            self.playerTurn = self.Player.WHITE
        else:
            self.playerTurn = self.Player.BLACK
        self.updateDisplay()


    def incrementTurnNumber(self):
        self.turnsNumber += 1
        self.display.setTurnNumber(self.turnsNumber)


if __name__ == "__main__":
    app = wx.App()
    game = Game()
    app.MainLoop()