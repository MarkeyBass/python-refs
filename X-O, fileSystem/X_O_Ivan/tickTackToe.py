def myFunc():
    print("hello")


def drawTickTackToeTable(moves):
    print(f"""
    _{moves[6]}_|_{moves[7]}_|_{moves[8]}_
    _{moves[3]}_|_{moves[4]}_|_{moves[5]}_
     {moves[0]} | {moves[1]} | {moves[2]}
    \n
            """)


def drawTickTackToeInstructions():
    print("""
    Choose a position to play.
    Your choice must be on an available cell.
    _7_|_8_|_9_
    _4_|_5_|_6_
     1 | 2 | 3
    \n
            """)


def getInputFromUser():
    while True:
        move = input("Make your choice:(1-9)")

        if move.isnumeric():
            move = int(move)
            if 0 < move < 10:
                return move - 1
        print('Input not valid - try again')


def validateMove(moves, move):
    vaild_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if (moves[move] in vaild_moves):
        return True
    else:
        return False


def checkIfWon(moves):
    for i in range(3):
        if moves[0 * (i + 1)] == moves[1 * (i + 1)] == moves[2 * (i + 1)] != '':
            return moves[1 * (i + 1)]
    if moves[0] == moves[3] == moves[6] != '':
        return moves[0]
    if moves[1] == moves[4] == moves[7] != '':
        return moves[1]
    if moves[2] == moves[5] == moves[8] != '':
        return moves[2]
    if moves[0] == moves[4] == moves[8] != '':
        return moves[0]
    if moves[2] == moves[4] == moves[6] != '':
        return moves[2]
    return False


if __name__ == '__main__':
    moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    drawTickTackToeInstructions()
    sign = ['X', 'O']
    move_counter = 0

    while True:
        move = getInputFromUser()
        if validateMove(moves, move):
            moves[move] = sign[move_counter % 2]
            move_counter += 1
        else:
            print("not valid move")
        drawTickTackToeTable(moves)
        winner = checkIfWon(moves)
        if winner:
            print(f'{winner} WON')
            break
