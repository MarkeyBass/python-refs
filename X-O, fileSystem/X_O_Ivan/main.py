import os
import copy
#
def readFile():
    file = open('hello.txt')
    data = file.read()
    file.close()
    return data

def saveToFile(ans):
    file = open('./ans.txt','w')
    file.write('Answer: ' + str(ans))
    file.close()
    return True


def findOcuurences(tarStr, locStr):
    count = 0

    if len(tarStr) > 1:
        analize = locStr.split(' ')
        for word in analize:
            if word.lower() == tarStr.lower():
                count += 1

    if len(tarStr) == 1:
        for letter in locStr:
            if letter == tarStr:
                count += 1

    return count


def tick_tack_toe(moves):
    # moves = ['','','','','','','','','']

    the_board = f"""
    _{moves[6]}_|_{moves[7]}_|_{moves[8]}_
    _{moves[3]}_|_{moves[4]}_|_{moves[5]}_
    _{moves[0]}_|_{moves[1]}_|_{moves[2]}_
                """
    print(the_board)

def isValidMove(move,sign):
    # print(moves[int(move)-1],sign)
    if not(int(move)>0 or int(move) <10) or not moves[int(move)-1]=='':
        print("Not valid move")
        return False
    else:
        return True

def check_if_won(moves):
    for i in range(3):
        if(moves[0*(i+1)]==moves[1*(i+1)]==moves[2*(i+1)]!=''):
            return moves[1*(i+1)]
    if(moves[0]==moves[3]==moves[6]!=''):
        return moves[0]
    if (moves[1] == moves[4] == moves[7]!=''):
        return moves[1]
    if (moves[2] == moves[5] == moves[8]!=''):
        return moves[2]
    if (moves[0] == moves[4] == moves[8]!=''):
        return moves[0]
    if (moves[2] == moves[4] == moves[6]!=''):
        return moves[2]
    return False
        
if __name__ == '__main__':
    # status = saveToFile(findOcuurences('lorem',readFile()))
    #
    # if(status):
    #     print(':)')
    # else:
    #     print(':(')

    # x = { 'details' : { 'fname' : 'ivan' , 'lname' : 'k' } , 'smth' : 'data' }
    # y = copy.deepcopy(x)
    # x['smth'] = 'new data'
    # x['details']['lname'] = 'kali'
    # print('X:'+x['smth'] +str(x['details']),'\nY:'+y['smth']+str(y['details']))

    moves = ['','','','','','','','','']
    sign = ['X','O']
    move_counter = 0
    while True:
        print(f'you play as {sign[move_counter%2]}')
        move = input("""choose a position to play
     _7_|_8_|_9_
     _4_|_5_|_6_
      1 | 2 | 3\n""")
        if(isValidMove(move,sign)):
            moves[int(move)-1] = sign[move_counter%2]
            move_counter+=1


        else:
            continue

        winner = check_if_won(moves)
        if( winner is not False):
            print(f'{winner} WON')
            break
        tick_tack_toe(moves)


