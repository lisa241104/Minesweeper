from pygame_minesweeper import PygameMinesweeper


def main_pygame():
    test = PygameMinesweeper(10, 10, 0, 0, (20, 20))
    test.play_game()


if __name__ == '__main__':
    main_pygame()
