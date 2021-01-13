import random

board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print(" " + board[1] + "| " + board[2] + "| " + board[3])
    print("_________")
    print(" " + board[4] + "| " + board[5] + "| " + board[6])
    print("_________")
    print(" " + board[7] + "| " + board[8] + "| " + board[9])

def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[6] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    while run:
        move = input('place x between 1-9')
        try:
            move = int(move)
            if 0 < move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('x', move)
                else:
                    print('Sorry, Occupied')
            else:
                print('Write a number in the range')
        except:
           print('Type a number!')

def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, 3)
    return li[r]

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['o', 'x']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = 1
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            edgesOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'o')):
            playerMove()
            
        else:
            print('Sorry, o won this time')
            break

        if not(isWinner(board, 'x')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('o', move)
                print('o has been placed', move , ':')
                printBoard(board)
        else:
            print('Sorry, x won this time')
            break

    if isBoardFull(board):
        print('Tie Game!')
