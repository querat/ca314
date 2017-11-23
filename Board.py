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

    def getSimpleArray(self):
        simpleArray = []
        for row in self.matrix:
            simpleRow = []
            for cell in row:
                simpleRow.append(cell.status)
            simpleArray.append(simpleRow)
        return simpleArray;

    def replace(self, array, val1 , val2):
        for row in array:
            for cell in row:
                if (cell == val1 || cell == val2):
                    cell = (cell == val1) ? (val2) : (val1)

    def calculScore(self):
        blackSimpleArray = self.getSimpleArray()
        whiteSimpleArray = self.replace(list(blackSimpleArray), Cell.Status.BLACK, Cell.Status.WHITE)

        blackNpArray = np.array(blackSimpleArray).astype(float)
        whiteNpArray = np.array(whiteSimpleArray).astype(float)

        resultBlackArray = fill.fast_fill(blackNpArray, four_way=True)
        resultWhiteArray = fill.fast_fill(whiteNpArray, four_way=True)

        print("Results:\n");
        print(resultBlackArray)
        print("")
        print(resultWhiteArray);
