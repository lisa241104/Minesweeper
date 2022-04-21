from minesweeper import Minesweeper
from cell import Cell
import pygame as pg
from load_image import load_image


class PygameMinesweeper(Minesweeper):

    def __init__(self, width, height, num_of_bombs, initial_opened_cells, margin: (int, int)):
        super().__init__(width, height, num_of_bombs, initial_opened_cells)

        # initialize pygame
        pg.init()
        self.screen = pg.display.set_mode((800, 600))

        # Margin of the board
        self.margin = margin
        # Positions of Cells that are calculated from row and column number
        self.positions = \
            [[(15 + margin[0] + 30 * a, 15 + margin[1] + 30 * b) for a in range(self.width)] for b in
             range(self.height)]
        # list of instance of Cell class
        self.cells = \
            [[Cell(pos=self.positions[r][c], row=r, column=c) for c in range(self.width)] for r in range(self.height)]

        self.screen = pg.display.set_mode((800, 600))

        self.mouse_down = False
        self.mouse_pos = (int, int)

    def display_board(self):
        for r in self.cells:
            for cell in r:
                cell.draw(self.screen)

    # parent class' make_board(), get_num_of_neighboring_bombs()

    def dig(self, cell):  # TODO: add the method to change the all cells' images
        if self.board[cell.row][cell.column] == 2:
            # if the cell is already flagged
            pass
        elif self.board[cell.row][cell.column] == 1:
            # if the cell is already opened
            pass
        else:
            if self.bombs[cell.row][cell.column] == -1:
                # if dug a bomb
                self.board = [[1 for _ in range(self.width)] for _ in range(self.height)]
                self.display_board()
                self.is_finished = True
            elif self.bombs[cell.row][cell.column] == 0:
                # if empty
                self.board[cell.row][cell.column] = 1
                self.opened_cells += 1
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if self.height > cell.row + a >= 0 and self.width > cell.column + b >= 0 \
                                and self.board[cell.row + a][cell.column + b] == 0:  # if neighboring cell is not opened
                            self.dig(self.cells[cell.row+a][cell.column+b])
            else:
                self.board[cell.row][cell.column] = 1
                self.opened_cells += 1

        image = load_image('GamePictures/1.png')
        cell.set_image(image)
        cell.draw(self.screen)

    def place_flag(self, row, column):
        # put flag on a selected cell
        if self.board[row][column] == 2:  # remove flag if already flagged
            self.board[row][column] = 0
        elif self.board[row][column] == 0:  # flag if the cell is closed and not flagged
            self.board[row][column] = 2

    def start_game(self):
        pass

    def play_game(self):
        self.display_board()

        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN and (not self.mouse_down):
                    self.mouse_down = True
                    self.mouse_pos = pg.mouse.get_pos()

            if self.is_finished:
                # if the game ended
                running = False

            if self.mouse_down:
                for r in self.cells:
                    for cell in r:
                        if cell.is_clicked(self.mouse_pos):
                            self.dig(cell)
                            self.mouse_down = False
                            break
                self.mouse_down = False

            pg.display.update()

        pg.quit()
