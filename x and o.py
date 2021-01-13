import random

board = [' ' for x in range(10)] ##List of the board positions

## Insert letter in a position for in the board
# (letter for the tokens and pos as the position in the  tictactoe board)
def insertLetter(letter, pos):
    board[pos] = letter

## Checks for free space in the tictactoe board
# (pos for the position in the tictactoe board)
def spaceIsFree(pos):
    return board[pos] == ' '

## Prints the tictactoe board on the terminal
def printBoard(board):
    print(" " + board[1] + "| " + board[2] + "| " + board[3])
    print("_________")
    print(" " + board[4] + "| " + board[5] + "| " + board[6])
    print("_________")
    print(" " + board[7] + "| " + board[8] + "| " + board[9])

## Checks for the winner in the board
# (bo for the tictactoe board and le for the letters in each board positions)
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[6] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

## Selecting the tokens point in the tictactoe board
def playerMove():
    run = True
    while run:
        # Code for the Token input from the user
        move = input('place x between 1-9: ')
        try:
            move = int(move)
            if 0 < move < 10: # Checks if move(user's input is greater than zero or less than ten)
                if spaceIsFree(move): ## checks if the user's input is free,
                    run = False ## and makes the run false,
                    insertLetter('x', move) ## Insert letter into the free space
                else:
                    print('Sorry, Occupied')
            else:
                print('Write a number in the range')
        except:
           print('Type a number!')

##Function to make the random choice for the computer
def random_choices(a_list):
    random_choice_index = random.randint(0, len(a_list) - 1)
    random_choice = a_list[random_choice_index]
    return random_choice


## Function to make the computer decide where to go
def computer_move_turn():
    tokens = "o"
    free_space_list = []
    for val in range(1, 10):
        if spaceIsFree(val) == True:
            free_space_list.append(val)
    insertLetter(tokens, random_choices(free_space_list))
    printBoard(board)


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
            computer_move_turn()
        else:
            print('Sorry, x won this time')
            break

    if isBoardFull(board):
        print('Tie Game!')

main()
