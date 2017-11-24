import  wx
from    enum import Enum
import  Game

class Cell:

    class Color(Enum):
        EMPTY       = 0
        WHITE       = 1
        BLACK       = 2


    Sprites = {
        Color.EMPTY : "res/cell-blank.png"
      , Color.WHITE : "res/cell-white.png"
      , Color.BLACK : "res/cell-black.png"
    }


    toString = {
        Color.EMPTY: "empty"
      , Color.WHITE: "white"
      , Color.BLACK: "black"
    }


    def __init__(self, xPos, yPos):
        self.status = Cell.Color.EMPTY
        self.xPos   = xPos
        self.yPos   = yPos


    def getColor(self):
        return self.status


    def getCurrentStatusSpritePath(self):
        return Cell.Sprites[self.status]


    def getXPos(self):
        return self.xPos


    def getYPos(self):
        return self.yPos


    def getPosition(self):
        return wx.Point(self.xPos, self.yPos)


    def setStatus(self, status):
        self.status = status


    def __str__(self):
        return self.toString[self.status]
