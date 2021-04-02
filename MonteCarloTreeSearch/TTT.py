"""
Author: Sean Dever
Date: 3/31/2021
Description: This program will serve as an example implementation of the Monte Carlo Tree Search using tic tac toe as our goal.
"""
import random # used for random player

class TTTBoard:
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.board = [['-'] * cols for row in range(rows)] # zero is the defualt space value

    def printBoard(self):
        print("=================")
        print("Tic Tac Toe Board")
        print("=================")
        for r in range(self.rows):
            for c in range(self.cols):
                print(self.board[r][c],end='')
            print()

    def makeMove(self,requestRow,requestCol,playerIcon):
        requestRow = int(requestRow)
        requestCol = int(requestCol)
        if(onBoard(self.rows,self.cols,requestRow,requestCol) and self.board[requestRow][requestCol] == '-'): # move must be on board and an empty spot
            self.board[requestRow][requestCol] = playerIcon
            return 1
        else:
            return 0

    def checkWin(self,playerIcon):
        # check win by row
        for row in range(self.rows):
            if((self.board[row][0] == playerIcon) and (self.board[row][1] == playerIcon) and (self.board[row][2] == playerIcon)):
                return playerIcon # win for playerIcon
        # check win by col
        for col in range(self.cols):
            if((self.board[0][col] == playerIcon) and (self.board[1][col] == playerIcon) and (self.board[2][col] == playerIcon)):
                return playerIcon
        # check win by diag
        if((self.board[0][0] == playerIcon) and (self.board[1][1] == playerIcon) and (self.board[2][2] == playerIcon)):
            return playerIcon
        if((self.board[2][0] == playerIcon) and (self.board[1][1] == playerIcon) and (self.board[0][2] == playerIcon)):
            return playerIcon
         
        return "0" # tie or loss


def onBoard(rows,cols,requestRow,requestCol): # ensure a move is legal
    if((requestRow >=0 and requestCol >= 0) and (requestRow <= rows-1) and (requestCol <= cols-1)):
        return True
    else:
        return False

def randomPlayerMove():
    # The random player will need to select a row and a col, we can use the random.random() function to generate a random decimal between 0 and 1. We will need three break points to catergorize each move
    # 1) 0 <-> .3333   2) .33331 <-> .6666 3) .66661 <-> .9999
    # default values
    row = 0 
    col = 0
    # random row
    randomNum = random.random()
    if(randomNum >= 0 and randomNum <= .3333):
        row = 0
    if(randomNum >= .33331 and randomNum <= .6666):
        row = 1
    if(randomNum >= .66661 and randomNum <= .9999):
        row = 2

    # random col
    randomNum = random.random()
    if(randomNum >= 0 and randomNum <= .3333):
        col = 0
    if(randomNum >= .33331 and randomNum <= .6666):
        col = 1
    if(randomNum >= .66661 and randomNum <= .9999):
        col = 2

    return row,col


# Entry Point
game = TTTBoard(3,3) # 2,2 is the bottom right corner

PLAYER1ICON = "X"
PLAYER2ICON = "O"

"""
#Testing Win Conditions
game.makeMove(1,1,PLAYER1ICON)
game.makeMove(0,1,PLAYER1ICON)
game.makeMove(2,1,PLAYER1ICON)

print(game.printBoard())

print(game.checkWin(PLAYER1ICON))

#Testing Random Player
randomRow, randomCol = randomPlayerMove()
print("Random Row: ",randomRow)
print("Random Col: ",randomCol)
"""
gameLoop = True
moveCount = 0
game.printBoard()

while(gameLoop):
    print()
    print("Player1 Select your move")
    player1Row = input("Row: ")
    player1Col = input("Col: ")
    print()

    validMove = game.makeMove(player1Row,player1Col,PLAYER1ICON) # Make Player 1 Move 
    while(validMove == 0):
        print("Invalid Move... Try again")
        player1Row = input("Row: ")
        player1Col = input("Col: ")
        validMove = game.makeMove(player1Row,player1Col,PLAYER1ICON) 

    game.printBoard() # print state of gameboard after player1's move

    if(game.checkWin(PLAYER1ICON) == "X"):
        print()
        print("Player 1 has won the game")
        print()
        gameLoop = False
        exit()
    
    print("Player2's move:")
    player2Row, player2Col = randomPlayerMove()
    
    validMove = game.makeMove(player2Row,player2Col,PLAYER2ICON)
    while(validMove == 0):
        player2Row, player2Col = randomPlayerMove()
        validMove = game.makeMove(player2Row,player2Col,PLAYER2ICON)
    
    print("Row: ",player2Row)
    print("Col: ",player2Col)
    print()

    gameLoop += 1
    game.printBoard() # print state of gameboard after player2's move 

    if(game.checkWin(PLAYER2ICON) == "O"):
        print()
        print("Player 2 have won the game") 
        print()
        gameLoop = False
        exit()

    if(moveCount == 9):
        print()
        print("The game has ended in a tie") 
        print()
        gameLoop = False
        exit()
   
