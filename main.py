# This code was created by Lisa Takahashi on 3/28/2022

from random import randint


class Minesweeper:
    def __init__(self, width, height, num_of_bombs, initial_opened_cells):
        # Todo: Make 2d array for boards and tuples to store which cells have been opened
        # Todo: Make variables for the width and height of the board and number of bombs
        self.width = width
        self.height = height
        self.num_of_bombs = num_of_bombs
        self.initial_opened_cells = initial_opened_cells

        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        # 0 = closed, 1 = opened
        self.bombs = [[0 for _ in range(self.width)] for _ in range(self.height)]
        # 0 = empty, -1 = bomb, numbers = number of neighboring bombs

    def display_board(self):
        # Todo: Prints the board
        print('□')

    def make_board(self):
        for _ in range(self.num_of_bombs):
            while True:
                row = randint(0, self.height)
                column = randint(0, self.width)
                if self.board[row][column] == -1:
                    pass  # if the selected cell is already a bomb, pass
                else:
                    self.board[row][column] = -1  # change to bomb
                    break

    def get_num_of_neighboring_bombs(self, row, column):
        # Todo: return number of bombs eight direction
        if self.board[row][column] == -1:
            return -1  # if it's bomb, return -1
        num = 0
        for a in range(-1, 2):
            for b in range(-1, 2):
                if self.board[row + a][column + b] == -1 and self.height > row + a >= 0 \
                        and self.width > column + b >= 0:
                    num += 1  # if index is negative, doesn't do this
        return num  # check neighboring cells in 8 direction and return the number of bombs

    def dig(self, row, column):
        # Todo: dig the cell and check if it's bomb, if not, check open neighboring cells if needed
        pass

    def start_game(self):
        # Todo: prints board for the first time. if the chosen cell has bomb or the opened cells are not many,
        #  create again
        pass

    def place_flag(self):
        # Todo: put flag on a selected cell
        pass

    def play_game(self):
        self.start_game()


print('# # ### ### ###  ## # # ### ### ### ### ##  ')
print('###  #  # # #   #   # # #   #   # # #   # # ')
print('###  #  # # ##   #  ### ##  ##  ### ##  ##  ')
print('# #  #  # # #     # ### #   #   #   #   # # ')
print('# # ### # # ### ##  # # ### ### #   ### # # ')

print('\nChoose level')

level_list = [[10, 8, 10, 0], [18, 14, 40, 0], [24, 20, 99, 0]]
# width, height, num_of_bombs, initial_opened_cells

while True:
    level = int(input('0: Easy, 1: Medium, 2: Hard\n'))  # A user will choose level
    try:
        new_game = Minesweeper(level_list[level][0], level_list[level][1], level_list[level][2], level_list[level][3])
        break
    except IndexError:
        print('Choose Valid Level')

new_game.play_game()
