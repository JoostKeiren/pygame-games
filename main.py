
import random

help(random)
print(random.randint(0, 1))
#board
board =[[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

#display board
def display_board():
    print(board[0][0]+"|"+board[0][1]+"|"+board[0][2])
    print("-----")
    print(board[1][0]+"|"+board[1][1]+"|"+board[1][2])
    print("-----")
    print(board[2][0]+"|"+board[2][1]+"|"+board[2][2])
display_board()
#continuous play
    #swich move
def swich_player(symbol):
    if symbol == "X":
        symbol = "O"
    elif symbol == "O":
        symbol = "X"
    return symbol


        #player1 move
def player_move(symbol):
      #check for valid input
    empty = False
    while empty is False:
        r, c = int(input("what row do yhou wnat to place?")), int(input("what collom do you want to place?"))
        if board[r][c] != "X" and board[r][c] != "O":
            board[r][c] = symbol          #check if place is empty
            empty = True
        else:
            print("invalid square try again")
    display_board()


#check win
def check_win(symbol):
    #horizontal win
    for a in range(3):
        if board[a][0] == board[a][1] == board[a][2] and not board[a][0] == " ":
            print("{} won".format(symbol))
            return True
        # vertical win
    for b in range(3):
        if board[0][b] == board[1][b] == board[2][b] and not board[0][b] == " ":
            print("{} won".format(symbol))
            return True
        # diagonal win
    if not board[1][1] == " " and (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]) :
        print("{} won".format(symbol))
        return True
    return False

    #check tie
def check_tie():
    found = False
    for a in range(3):
        for b in range(3):
            if board[a][b] == " ":
                found = True

    if ((found is False) and (check_win() is False)):
        print("its a tie!")
        return True
    return False

sym = "O"
while not check_win(sym) and not check_tie():
    sym = swich_player(sym)
    player_move(sym)
    print(check_win(sym))
    print(check_tie())