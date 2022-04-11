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
        self.is_finished = False

        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        # 0 = closed, 1 = opened, 2 = flag
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
                if self.board[n][m] == 0:  # closed
                    print('-  ', end='')
                elif self.board[n][m] == 2:  # flag
                    print('F  ', end='')
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
        if self.board[row][column] == 2:
            print('This cell is flaged')
        elif self.board[row][column] == 1:
            pass
        else:
            if self.bombs[row][column] == -1:
                print('You dug a bomb')
                self.board = [[1 for _ in range(self.width)] for _ in range(self.height)]
                self.display_board()
                self.is_finished = True
            elif self.bombs[row][column] == 0:
                self.board[row][column] = 1
                self.opened_cells += 1
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if self.height > row + a >= 0 and self.width > column + b >= 0 \
                                and self.board[row + a][column + b] == 0:  # if neighboring cell is not opened
                            self.dig(row + a, column + b)  # dig that cell
                        else:
                            pass
            else:  # if the cell is not bombs and there is no bombs in eight directions
                self.board[row][column] = 1
                self.opened_cells += 1

    def start_game(self):
        # prints board for the first time. if the chosen cell has bomb or the opened cells are not many, create again
        self.display_board()
        while True:
            user_input = input("Choose the cell (row column) ex. Ac\n")
            user_input = user_input.lower()
            try:
                selected = [ord(user_input[0]) - 97, ord(user_input[1]) - 97]  # row, column
                _ = self.bombs[selected[0]][selected[1]]
                break
            except IndexError:
                print('Enter Valid Coordinate')
        finished_making_board = False
        while not finished_making_board:
            self.make_board()
            if self.bombs[selected[0]][selected[1]] != 0:
                self.bombs = [[0 for _ in range(self.width)] for _ in range(self.height)]  # reset board
            else:
                self.dig(selected[0], selected[1])
                if self.opened_cells < self.initial_opened_cells:
                    self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
                    self.bombs = [[0 for _ in range(self.width)] for _ in range(self.height)]
                    self.opened_cells = 0  # recreate board if enough cells are not opened
                else:
                    finished_making_board = True

    def place_flag(self, row, column):
        # put flag on a selected cell
        if self.board[row][column] == 2:
            self.board[row][column] = 0
        elif self.board[row][column] == 1:
            print('This cell is opened')
        else:
            self.board[row][column] = 2

    def play_game(self):
        self.start_game()
        while not self.is_finished:
            self.display_board()

            choice_dig = False
            choice_flag = False
            while True:
                user = input('Enter command: Dig / Place (remove) a flag / Exit from the game\nd/f/exit\n')
                if user == 'exit':
                    self.is_finished = True
                    return 0
                elif user == 'd':
                    choice_dig = True
                    break
                elif user == 'f':
                    choice_flag = True
                    break
                else:
                    print('Enter valid command')

            while True:
                user_input = input("Choose the cell (row column) ex. Ac\n")
                try:
                    user_input = user_input.lower()
                    selected = [ord(user_input[0]) - 97, ord(user_input[1]) - 97]  # row, column
                    if choice_dig:
                        self.dig(selected[0], selected[1])
                    elif choice_flag:
                        self.place_flag(selected[0], selected[1])
                    else:
                        pass
                    break
                except IndexError:
                    print('Enter Valid Coordinate')

            if self.opened_cells >= (self.height * self.width - self.num_of_bombs):  # if all bombs are detected
                print("Congratulation! You found all bombs!")
                self.board = [[1 for _ in range(self.width)] for _ in range(self.height)]
                self.display_board()
                self.is_finished = True


print('# # ### ### ###  ## # # ### ### ### ### ##  ')
print('###  #  # # #   #   # # #   #   # # #   # # ')
print('###  #  # # ##   #  ### ##  ##  ### ##  ##  ')
print('# #  #  # # #     # ### #   #   #   #   # # ')
print('# # ### # # ### ##  # # ### ### #   ### # # ')

level_list = [[7, 5, 5, 0], [10, 8, 10, 13], [18, 14, 40, 17], [24, 20, 99, 37]]
# width, height, num_of_bombs, initial_opened_cells
restart = True

while restart:
    print('\nChoose level')

    while True:
        level = input('0: Easy (5*5, 4 bombs), 1: Medium (10*8, 10 bombs), '
                      '2: Hard (18*14, 40 bombs), 3: Expert (24*20, 99 bombs)\n')  # A user will choose level
        try:
            level = int(level)
            new_game = Minesweeper(level_list[level][0], level_list[level][1],
                                   level_list[level][2], level_list[level][3])
            break
        except IndexError:
            print('Choose Valid Level')
        except ValueError:
            print('Choose Valid Level')

    new_game.play_game()

    user_choice = input('Restart? y/n\n')
    if user_choice != 'y':
        print('Thank you for playing!')
        restart = False
