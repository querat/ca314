import numpy as np
# import pytest

import fill


def test_fast_fill_8way():
    init = np.array([
        [2, 1, 1, 1, 1, 2],
        [2, 1, 1, 2, 1, 2],
        [2, 1, 1, 2, 1, 2],
        [2, 1, 1, 2, 1, 2],
        [2, 1, 1, 2, 1, 2],
        [2, 1, 1, 1, 1, 2],
        ]).astype(float)
    white = np.array(init)
    black = np.array(init)

    for x in range(0, len(white)):
        for y in range(0, len(white)):
            if white[x, y] == 2.0:
                white[x, y] = 0.5

    for x in range(0, len(black)):
        for y in range(0, len(black)):
            if black[x, y] == 2.0:
                black[x, y] = 1.0
            elif black[x, y] == 1.0:
                black[x, y] = 0.5

    print("white")
    print(white)
    print("")
    print(fill.fast_fill(white, four_way=True))
    print("")
    print("black")
    print(black)
    print("")
    print(fill.fast_fill(black, four_way=True))


test_fast_fill_8way()