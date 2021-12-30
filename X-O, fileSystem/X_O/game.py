# X / O Game:
# ============

def func_validation(player):
    win_validation = (['1', '2', '3'] or ['4', '5', '6'] or
                      ['7', '8', '9'] or ['7', '4', '1'] or
                      ['8', '5', '2'] or ['9', '6', '3'] or
                      ['7', '5', '3'] or ['9', '5', '1'])
    valid_win = all(item in player for item in win_validation)
    return valid_win


complete = False
x_list = []
o_list = []
board_game = """

    enter your choice: 

            _7_|_8_|_9_
            _4_|_5_|_6_
             1 | 2 | 3

        """

if __name__ == '__main__':
    while not complete:
        print(board_game)
        x = input('player X: ')
        board_game = board_game.replace(x, 'X')
        x_list.append(x)
        if func_validation(x_list):
            print(board_game)
            print('X is the winner!!!')
            break

        print(board_game)
        o = input('player O: ')
        board_game = board_game.replace(o, 'O')
        o_list.append(o)
        if func_validation(o_list):
            print(board_game)
            print('O is the winner!!!')
            complete = True
