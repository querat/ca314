import numpy as np
import  Config
import fill
import copy
from    Cell   import Cell

class Board:

    def __init__(self):
        # 2D array of Cells
        self.matrix = [[Cell(x, y) for x in range(Config.NB_COLS)] for y in range(Config.NB_ROWS) ]
        # will disappear
        self.testPopulate()
        self.calculScore()

    # Will disappear, just testing sprites
    def testPopulate(self):
        from random import randint
        for row in self.matrix:
            for cell in row:
                cell.setStatus(Cell.Status(randint(0, 2)))

    def getMatrix(self):
        return self.matrix

    def getPlayersScores(self, finalArray):
        whitePlayerScore = 7.5
        blackPlayerScore = 0.0

        for y in range(0, len(finalArray)):
            for x in range(0, len(finalArray[y])):
                if finalArray[y,x] == Cell.Status.BLACK.value:
                    blackPlayerScore += 1.0
                elif finalArray[y,x] == Cell.Status.WHITE.value:
                    whitePlayerScore += 1.0
        return whitePlayerScore, blackPlayerScore

    def getSimpleArray(self):
        simpleArray = []
        for row in self.matrix:
            simpleRow = []
            for cell in row:
                simpleRow.append(cell.status.value)
            simpleArray.append(simpleRow)
        return simpleArray

    def replace(self, array, val1 , val2):
        for y, row in enumerate(array):
            for x, cell in enumerate(row):
                if cell != Cell.Status.EMPTY.value:
                    array[y][x] = val2 if cell == val1 else val1
        return array

    def calculScore(self):
        blackSimpleArray = self.getSimpleArray()
        whiteSimpleArray = self.replace(copy.deepcopy(blackSimpleArray), Cell.Status.BLACK.value, Cell.Status.WHITE.value)

        resultBlackArray = fill.fast_fill(np.array(blackSimpleArray))
        resultWhiteArray = fill.fast_fill(np.array(whiteSimpleArray))

        finalArray = np.array([[0 for x in range(Config.NB_COLS)] for y in range(Config.NB_ROWS)])

        for y in range(0, len(resultWhiteArray)):
            for x in range(0, len(resultWhiteArray[y])):
                if resultBlackArray[y,x] == resultWhiteArray[y,x] and resultBlackArray[y,x] != 0:
                    finalArray[y,x] = 0
                else:
                    finalArray[y,x] = resultBlackArray[y,x]

        print(self.getPlayersScores(finalArray))
