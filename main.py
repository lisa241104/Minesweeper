# This code was created by Lisa Takahashi on 3/28/2022

from minesweeper import Minesweeper


def main():
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
            level = input('0: Easy (7*5, 5 bombs), 1: Medium (10*8, 10 bombs), '
                          '2: Hard (18*14, 40 bombs), 3: Expert (24*20, 99 bombs)\n')  # A user will choose level
            try:
                level = int(level)
                new_game = Minesweeper(*level_list[level])
                # = level_list[level][0], level_list[level][1], level_list[level][2], level_list[level][3]
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


if __name__ == '__main__':
    main()
