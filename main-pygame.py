from pygame_minesweeper import PygameMinesweeper
import pygame as pg


def main_pygame():
    test = PygameMinesweeper(10, 8, 10, 13, (20, 20))
    test.play_game()


if __name__ == '__main__':
    main_pygame()
