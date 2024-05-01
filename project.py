board=['_' for i in range(9)]
def displayboard():
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("|", board[6], "|", board[7], "|", board[8], "|")

player1="x"
player2="o"

def startgame():
    while True:
        while True:

        player1_option=input(f"{player1},enter your position: ")
        if board[int(player1_option)-1]=="_":
            board[int(player1_option)-1]==player1
            displayBoard()
            break

        else:
            print("This place is not empty !")

startgame()