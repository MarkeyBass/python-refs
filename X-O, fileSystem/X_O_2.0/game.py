# X / O Game:
# ============
x_list = []
o_list = []
available_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
board_game = """
    enter your choice: 

            _7_|_8_|_9_
            _4_|_5_|_6_
             1 | 2 | 3
        """


def is_winner(player):
    win_validations = [
        ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3'], ['7', '5', '3'], ['9', '5', '1']
    ]
    for validation in win_validations:
        valid_win = all(item in player for item in validation)
        if valid_win:
            return valid_win
    return False


def is_available_move(move):
    if move.isnumeric() and 0 < int(move) < 10:
        if move in available_moves:
            available_moves.remove(move)
            return True

    return False


def players_move(ui, players_symbol, players_list):
    playerComplete = False
    while not playerComplete:
        print(ui)
        move = input(f'player {players_symbol}: ')
        if is_available_move(move):
            ui = ui.replace(move, f'{players_symbol}')
            players_list.append(move)
            playerComplete = True
        else:
            print('Unavailable move, try again.')
    if is_winner(players_list):
        print(ui)
        print(f'{players_symbol} is the winner!!!')
        return 'game over'
    return [ui, players_list]


if __name__ == '__main__':
    playersValues = [['X', 'O'], [x_list, o_list]]
    counter = 2

    while True:
        result = players_move(board_game, playersValues[0][counter % 2], playersValues[1][counter % 2])
        counter += 1
        if result == 'game over':
            print(result)
            break
        else:
            board_game = result[0]
            x_list = result[1]


# # VERSION 2.0 - players_move() function is required

# if __name__ == '__main__':
#     while True:
#         x = players_move(board_game, 'X', x_list)
#         if x == 'game over':
#             print(x)
#             break
#         else:
#             board_game = x[0]
#             x_list = x[1]
#         o = players_move(board_game, 'O', o_list)
#         if o == 'game over':
#             print(o)
#             break
#         else:
#             board_game = o[0]
#             o_list = o[1]


# # VERSION 1.0 - players_move() function is NOT required

# if __name__ == '__main__':
#     while True:
#         xComplete = False
#         while not xComplete:
#             print(board_game)
#             x = input('player X: ')
#             if is_available_move(x):
#                 board_game = board_game.replace(x, 'X')
#                 x_list.append(x)
#                 xComplete = True
#             else:
#                 print('Unavailable move, try again.')
#         if is_winner(x_list):
#             print(board_game)
#             print('X is the winner!!!')
#             break
#
#         oComplete = False
#         while not oComplete:
#             print(board_game)
#             o = input('player O: ')
#             if is_available_move(o):
#                 board_game = board_game.replace(o, 'O')
#                 o_list.append(o)
#                 oComplete = True
#             else:
#                 print('Unavailable move, try again.')
#         if is_winner(o_list):
#             print(board_game)
#             print('O is the winner!!!')
#             break

