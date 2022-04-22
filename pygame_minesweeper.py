from minesweeper import Minesweeper
from cell import Cell
import pygame as pg
from load_image import load_image


class PygameMinesweeper(Minesweeper):
    def __init__(self, width, height, num_of_bombs, initial_opened_cells, margin: (int, int)):
        super().__init__(width, height, num_of_bombs, initial_opened_cells)

        # initialize pygame
        pg.init()
        self.screen = pg.display.set_mode((self.width*30+margin[0]*2, self.height*30+margin[1]*2))

        # Margin of the board
        self.margin = margin
        # Positions of Cells that are calculated from row and column number
        self.positions = \
            [[(15 + margin[0] + 30 * a, 15 + margin[1] + 30 * b) for a in range(self.width)]
             for b in range(self.height)]
        # list of instance of Cell class
        self.cells = \
            [[Cell(pos=self.positions[r][c], row=r, column=c) for c in range(self.width)]
             for r in range(self.height)]

        self.game_started = False
        self.mouse_down = False
        self.mouse_pos = (int, int)
        self.right_click = False

    def display_board(self):
        if self.is_finished:
            for r in self.cells:
                for cell in r:
                    cell.revealed(self.screen)
        else:
            for r in self.cells:
                for cell in r:
                    cell.draw(self.screen)

    def make_board(self):
        super().make_board()
        for r in range(self.height):
            for c in range(self.width):
                if self.bombs[r][c] == -1:
                    self.cells[r][c].status = 'bomb'
                elif self.bombs[r][c] == 0:
                    self.cells[r][c].status = 'empty'
                elif self.bombs[r][c] == 1:
                    self.cells[r][c].status = '1'
                elif self.bombs[r][c] == 2:
                    self.cells[r][c].status = '2'
                elif self.bombs[r][c] == 3:
                    self.cells[r][c].status = '3'
                elif self.bombs[r][c] == 4:
                    self.cells[r][c].status = '4'
                elif self.bombs[r][c] == 5:
                    self.cells[r][c].status = '5'
                elif self.bombs[r][c] == 6:
                    self.cells[r][c].status = '6'
                elif self.bombs[r][c] == 7:
                    self.cells[r][c].status = '7'
                elif self.bombs[r][c] == 8:
                    self.cells[r][c].status = '8'

    # parent class' get_num_of_neighboring_bombs()

    def dig(self, row, column):
        cell = self.cells[row][column]
        if self.board[row][column] == 2:
            # if the cell is already flagged
            pass
        elif self.board[row][column] == 1:
            # if the cell is already opened
            pass
        else:
            if self.bombs[row][column] == -1:
                # if dug a bomb
                self.is_finished = True
                self.display_board()
            elif self.bombs[row][column] == 0:
                # if empty
                self.board[row][column] = 1
                self.opened_cells += 1
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if self.height > row + a >= 0 and self.width > column + b >= 0 \
                                and self.board[row + a][column + b] == 0:  # if neighboring cell is not opened
                            self.dig(row+a, column+b)
            else:
                self.board[row][column] = 1
                self.opened_cells += 1

        cell.revealed(self.screen)

    def place_flag(self, row, column):
        # put flag on a selected cell
        if self.board[row][column] == 2:  # remove flag if already flagged
            self.board[row][column] = 0
            cell = self.cells[row][column]
            cell.flag = False
            cell.image = load_image('GamePictures/empty.png')
            cell.draw(self.screen)
        elif self.board[row][column] == 0:  # flag if the cell is closed and not flagged
            self.board[row][column] = 2
            cell = self.cells[row][column]
            cell.flag = True
            cell.revealed(self.screen)

    def start_game(self):
        self.display_board()
        self.make_board()

    def play_game(self):
        self.start_game()

        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN and (not self.mouse_down):
                    self.mouse_down = True
                    self.mouse_pos = pg.mouse.get_pos()
                    if event.button == 3:
                        self.right_click = True

            if self.opened_cells >= (self.height * self.width - self.num_of_bombs):
                # if all bombs are detected
                self.is_finished = True
                self.display_board()

            if self.is_finished:
                # if the game ended
                running = False

            if not self.game_started and self.mouse_down:
                finished_making_board = False
                while not finished_making_board:
                    for r in self.cells:
                        for cell in r:
                            if cell.is_clicked(self.mouse_pos):
                                if self.bombs[cell.row][cell.column] != 0:
                                    self.bombs = [[0 for _ in range(self.width)] for _ in range(self.height)]
                                else:
                                    self.dig(cell.row, cell.column)
                                break
                    if self.opened_cells < self.initial_opened_cells:
                        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
                        self.bombs = [[0 for _ in range(self.width)] for _ in range(self.height)]
                        self.opened_cells = 0  # recreate board if enough cells are not opened
                        self.make_board()
                    else:
                        finished_making_board = True
                self.mouse_down = False
                self.right_click = False
                self.game_started = True

            if self.mouse_down and not self.right_click:
                for r in self.cells:
                    for cell in r:
                        if cell.is_clicked(self.mouse_pos):
                            self.dig(cell.row, cell.column)
                            self.mouse_down = False
                            break
                self.mouse_down = False
            elif self.mouse_down and self.right_click:
                for r in self.cells:
                    for cell in r:
                        if cell.is_clicked(self.mouse_pos):
                            self.place_flag(cell.row, cell.column)
                            self.mouse_down = False
                            break
                self.mouse_down = False
                self.right_click = False

            pg.display.update()
