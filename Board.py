import  Config
from    Cell   import Cell

class Board:

    def __init__(self):
        # 2D array of Cells
        self.matrix = [[Cell(x, y) for x in range(Config.NB_COLS)] for y in range(Config.NB_ROWS) ]
        # will disappear
        self.testPopulate()

    # Will disappear, just testing sprites
    def testPopulate(self):
        from random import randint
        for row in self.matrix:
            for cell in row:
                cell.setStatus(Cell.Status(randint(0, 2)))

    def getMatrix(self):
        return self.matrix