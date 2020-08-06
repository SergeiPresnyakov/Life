import random
import copy
import os
import time


# constants
FIELD_SIZE = 50
ALIFE_CELL_CHAR = 'o'
R_PENTHAMINO_COORDS = (
        (22, 21),
        (22, 22),
        (23, 20),
        (23, 21),
        (24, 21)
    )


class Field:
    def __init__(self):
        self.board = [[' '] * FIELD_SIZE for _ in range(FIELD_SIZE)]
        for x, y in R_PENTHAMINO_COORDS:
            self.board[x][y] = ALIFE_CELL_CHAR
 
    def __str__(self):
        for row in self.board:
            print(*row)
        return ''
    
    def do_step(self):
        # show board before each step
        print(self)

        # next step forming in self.cboard - copy of self.board
        # after step is done, they sweep places
        self.cboard = copy.deepcopy(self.board)
        for i in range(FIELD_SIZE):
            for j in range(FIELD_SIZE):
                self.cboard[i][j] = self.__test_cell(i, j)

        # if nothing changed
        if self.board == self.cboard:
            exit(0)

        self.board = copy.deepcopy(self.cboard)
    
    def __test_cell(self, i, j):
        alives = self.__count_alive_neighbors(i, j)
        if self.board[i][j] == ' ' and alives == 3:
            return ALIFE_CELL_CHAR
        elif self.board[i][j] == ALIFE_CELL_CHAR and (alives < 2 or alives > 3):
            return ' '
        else:
            return self.board[i][j]
    
    def __count_alive_neighbors(self, i, j):
        # index corrections for i, j to get neighbors
        index_corrections = (
            (-1, -1),
            (-1, 0),
            (-1, 1 if j < FIELD_SIZE - 1 else -FIELD_SIZE),
            (0, -1),
            (0, 1 if j < FIELD_SIZE - 1 else -FIELD_SIZE),
            (1 if i < FIELD_SIZE - 1 else -FIELD_SIZE, -1),
            (1 if i < FIELD_SIZE - 1 else -FIELD_SIZE, 0),
            (1 if i < FIELD_SIZE - 1 else -FIELD_SIZE, 1 if j < FIELD_SIZE - 1 else -FIELD_SIZE)
        )
        
        alives = 0
        for k, m in index_corrections:
            if self.board[i+k][j+m] == ALIFE_CELL_CHAR:
                alives += 1
        return alives


def main():
    game = Field()
    for _ in range(1000):
        game.do_step()
        time.sleep(0.1)
        os.system('cls')


if __name__ == '__main__':
    main()