
from random import randint, random
from termcolor import colored
import time

def test_positionOnBoard():
    assert positionOnBoard(5) == (2,2), "Should be (2,2)"

def positionOnBoard(position):
    if position == 1: # top
        positionX = 1
        positionY = 1
    elif position == 2:
        positionX = 2
        positionY = 1
    elif position == 3:
        positionX = 3
        positionY = 1
    elif position == 4:
        positionX = 1
        positionY = 2
    elif position == 5:
        positionX = 2
        positionY = 2
    elif position == 6:
        positionX = 3
        positionY = 2
    elif position == 7:
        positionX = 1
        positionY = 3
    elif position == 8:
        positionX = 2
        positionY = 3
    else:
        positionX = 3
        positionY = 3

    return (positionY, positionX)

def test_is_this_position_free():
    board = [["_","_","_"],["_","_","_"],["_","_","_"]]
    board[1][1] = colored("x", 'red')
    assert is_this_position_free(board, (2,2)) == ("-1", "-1"), "Should be (-1, -1)"
    assert is_this_position_free(board,(1,1)) == (1,1), "Should be (1,1)"

def is_this_position_free(board, position):
    x = colored("x", 'red')
    o = colored("o", 'green')
    positionX = position[1]
    positionY = position[0]
    if board[positionY-1][positionX-1] != x and board[positionY-1][positionX-1] != o:
        return position
    else:
        return ("-1", "-1")

def test_player_move():
    player = 1
    position = 5
    board = [["_","_","_"],["_","_","_"],["_","_","_"]]
    board[1][1] = colored("x", 'red')
    assert player_move(player, position, board) == (board, False), "Should be (Board False)"
    
    player = 2
    position = 5
    board = [["_","_","_"],["_","_","_"],["_","_","_"]]
    correct_board = [["_","_","_"],["_","_","_"],["_","_","_"]]
    positionXY = is_this_position_free(board, positionOnBoard(position))

    correct_board[positionXY[0]-1][positionXY[1]-1] = colored("o", "green")
    result = (correct_board, True)
    assert player_move(player, position, board) == (correct_board, True), "Should be (Board True)"


def player_move(player, position, board):
    x = colored("x", 'red')
    o = colored("o", 'green')
    positionXY = is_this_position_free(board, positionOnBoard(position))
    if positionXY[0] != "-1" or positionXY[1] != "-1":
        if player == 1:
            board[positionXY[0]-1][positionXY[1]-1] = x
        elif player == 2:
            board[positionXY[0]-1][positionXY[1]-1] = o
        return (board, True)
    else:
        return (board, False)

def test_whoWin():
    boardWinBlue = [["_","_","_"],["_","_","_"],["_","_","_"]]
    boardWin = [["_","_","_"],["_","_","_"],["_","_","_"]]
    for i in range(0,3):
        boardWin[2][i] = colored("x", 'red')
        boardWinBlue[2][i] = colored("x", 'blue')

    assert whoWin(boardWin) == (True, colored("x", 'red'), boardWinBlue), "Should be (True, player, board)"

    boardClear = [["_","_","_"],["_","_","_"],["_","_","_"]]
    assert whoWin(boardClear) == (False, 0, boardClear), "Should be (False, 0, boardClear)"


def whoWin(board):
    x = colored("x", 'red')
    o = colored("o", 'green')
    for player in (x, o):
        for i in (0,1,2):
            if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                board[i][0] = colored("x", 'blue') if player == x else colored("o", 'blue') 
                board[i][1] = colored("x", 'blue') if player == x else colored("o", 'blue')
                board[i][2] = colored("x", 'blue') if player == x else colored("o", 'blue')
                return (True, player, board)
            elif board[0][i] == player and board[1][i] == player and board[2][i] == player:
                board[0][i] = colored("x", 'blue') if player == x else colored("o", 'blue')
                board[1][i] = colored("x", 'blue') if player == x else colored("o", 'blue')
                board[2][i] = colored("x", 'blue') if player == x else colored("o", 'blue')
                return (True, player, board)
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                board[0][0] = colored("x", 'blue') if player == x else colored("o", 'blue')
                board[1][1] = colored("x", 'blue') if player == x else colored("o", 'blue')
                board[2][2] = colored("x", 'blue') if player == x else colored("o", 'blue')
                return (True, player, board)
        elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
                board[0][2] = colored("x", 'blue') if player == x else colored("o", 'blue')
                board[1][1] = colored("x", 'blue') if player == x else colored("o", 'blue')
                board[2][0] = colored("x", 'blue') if player == x else colored("o", 'blue')
                return (True, player, board)   
    return (False, 0, board)

def display(board, example):
    print('\x1bc')
    print("Game", "\t\t\t", "Example")
    print(board[0][0],"|", board[0][1],"|", board[0][2], "\t||\t", example[0][0],"|", example[0][1],"|", example[0][2])
    print("----------")
    print(board[1][0],"|", board[1][1],"|", board[1][2], "\t||\t", example[1][0],"|", example[1][1],"|", example[1][2])
    print("----------")
    print(board[2][0],"|", board[2][1],"|", board[2][2], "\t||\t", example[2][0],"|", example[2][1],"|", example[2][2])


def displayWin(board):
    print('\x1bc')
    print(board[0][0],"|", board[0][1],"|", board[0][2])
    print("----------")
    print(board[1][0],"|", board[1][1],"|", board[1][2])
    print("----------")
    print(board[2][0],"|", board[2][1],"|", board[2][2])

if __name__ == "__main__":
    test_positionOnBoard()
    test_is_this_position_free()
    test_player_move()
    test_whoWin()
    print("Everything passed")

# Main program
example = [["1","2","3"],["4","5","6"],["7","8","9"]]
board = [["_","_","_"],["_","_","_"],["_","_","_"]]
posible_moves = 9

x = colored("x", 'red')
o = colored("o", 'green')

while 1:
    if posible_moves > 0:
        display(board, example)
        print("\n"+x+" move:") if posible_moves % 2 + 1 == 1 else print("\n"+o+" move:") 
        if posible_moves % 2 + 1 == 1:
            player_move_correct = player_move(posible_moves % 2 + 1, randint(1,9), board) #
        else:
            if posible_moves == 9:                
                player_move_correct = player_move(posible_moves % 2 + 1, randint(1,9), board)
            else:
                player_move_correct = player_move(posible_moves % 2 + 1, randint(1,9), board)

        if player_move_correct[1] == True:
            board = player_move_correct[0]
            iswin = whoWin(board)
            if iswin[0] == True:
                displayWin(iswin[2])
                print("Win person who playd sign: ",iswin[1])
                break
            display(board, example)
            posible_moves -= 1
        else:
            print("This position is used already, pick another one")
            time.sleep(1)

    else:
        print("Draw")
        break
