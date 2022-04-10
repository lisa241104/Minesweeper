# This code was created by Lisa Takahashi on 3/28/2022

from random import randint
import string


class Minesweeper:
    def __init__(self, width, height, num_of_bombs, initial_opened_cells):
        self.width = width
        self.height = height
        self.num_of_bombs = num_of_bombs
        self.initial_opened_cells = initial_opened_cells

        self.opened_cells = 0
        self.isFinished = False

        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        # 0 = closed, 1 = opened
        self.bombs = [[0 for _ in range(self.width)] for _ in range(self.height)]
        # 0 = empty, -1 = bomb, numbers = number of neighboring bombs

    def display_board(self):
        upper_alphabet_string = list(string.ascii_uppercase)
        lower_alphabet_string = list(string.ascii_lowercase)
        print('   ' + '  '.join(lower_alphabet_string[:self.width]), end='')
        for (label, n) in zip(upper_alphabet_string[:self.height], range(self.height)):
            print('\n' + label, end='  ')
            # if the cell is not opened, print '-' and if the cell is opened, print the num of neighboring bombs
            for m in range(self.width):
                if self.board[n][m] == 0:
                    print('-  ', end='')
                else:
                    if self.bombs[n][m] == 0:
                        print('   ', end='')
                    elif self.bombs[n][m] == -1:
                        print('*  ', end='')
                    else:
                        print(str(self.bombs[n][m]) + '  ', end='')
        print('\n')

    def make_board(self):
        for _ in range(self.num_of_bombs):
            while True:
                n = randint(0, self.height - 1)
                m = randint(0, self.width - 1)
                if self.bombs[n][m] == -1:
                    pass  # if the selected cell is already a bomb, pass
                else:
                    self.bombs[n][m] = -1  # change to bomb
                    break
        # apply get_num_of_neighboring_bombs
        for n in range(self.height):
            for m in range(self.width):
                self.bombs[n][m] = self.get_num_of_neighboring_bombs(n, m)

    def get_num_of_neighboring_bombs(self, row, column):
        # Todo: return number of bombs eight direction
        if self.bombs[row][column] == -1:
            return -1  # if it's bomb, return -1
        num = 0
        for a in range(-1, 2):
            for b in range(-1, 2):
                if self.height > row + a >= 0 and self.width > column + b >= 0 \
                        and self.bombs[row + a][column + b] == -1:
                    num += 1  # if index is out of range, skip this
        return num  # check neighboring cells in 8 direction and return the number of bombs

    def dig(self, row, column):
        # Todo: open the cell and check if it's bomb, if not, check neighboring cells if needed
        if self.bombs[row][column] == -1:
            pass  # write a code to finish game
        elif self.bombs[row][column] != 0:
            self.board[row][column] = 1
            self.opened_cells += 1
        else:  # if the cell is not bombs and there is no bombs in eight directions
            self.board[row][column] = 1
            self.opened_cells += 1
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if self.height > row + a >= 0 and self.width > column + b >= 0 \
                            and self.board[row + a][column + b] == 0:  # if neighboring cell is not opened
                        self.dig(row + a, column + b)  # dig that cell

    def start_game(self):
        # Todo: prints board for the first time. if the chosen cell has bomb or the opened cells are not many,
        #  create again
        self.display_board()
        user_input = input("Choose the cell (row column) ex. Ac\n")
        user_input = user_input.lower()
        selected = [ord(user_input[0]) - 97, ord(user_input[1]) - 97]  # row, column
        while True:
            self.make_board()
            if self.bombs[selected[0]][selected[1]] == -1:
                self.bombs = [[0 for _ in range(self.width)] for _ in range(self.height)]  # reset board
                pass  # recreate board if selected cell is bombs
            else:
                self.dig(selected[0], selected[1])
                if self.opened_cells < self.initial_opened_cells:
                    self.bombs = [[0 for _ in range(self.width)] for _ in range(self.height)]
                    pass  # recreate board if enough cells are not opened
                else:
                    break

    def place_flag(self):
        # Todo: put flag on a selected cell
        pass

    def play_game(self):
        self.start_game()
        while not self.isFinished:
            self.display_board()
            break


print('# # ### ### ###  ## # # ### ### ### ### ##  ')
print('###  #  # # #   #   # # #   #   # # #   # # ')
print('###  #  # # ##   #  ### ##  ##  ### ##  ##  ')
print('# #  #  # # #     # ### #   #   #   #   # # ')
print('# # ### # # ### ##  # # ### ### #   ### # # ')

print('\nChoose level')

level_list = [[10, 8, 10, 10], [18, 14, 40, 0], [24, 20, 99, 0], [3, 3, 1, 0]]
# width, height, num_of_bombs, initial_opened_cells

while True:
    level = input('0: Easy, 1: Medium, 2: Hard\n')  # A user will choose level
    try:
        level = int(level)
        new_game = Minesweeper(level_list[level][0], level_list[level][1], level_list[level][2], level_list[level][3])
        break
    except IndexError:
        print('Choose Valid Level')
    except ValueError:
        print('Choose Valid Level')

new_game.play_game()
