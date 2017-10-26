from enum import Enum

class Cell:

    class Status(Enum):
        EMPTY       = 0
        WHITE       = 1
        BLACK       = 2

    Sprites = {
        Status.EMPTY : "res/cell-blank.png"
      , Status.WHITE : "res/cell-white.png"
      , Status.BLACK : "res/cell-black.png"
    }

    def __init__(self, xPos, yPos):
        self.status = Cell.Status.EMPTY
        self.xPos   = xPos
        self.yPos   = yPos

    def getCurrentStatusSpritePath(self):
        return Cell.Sprites[self.status]

    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos

    def setStatus(self, status):
        self.status = status