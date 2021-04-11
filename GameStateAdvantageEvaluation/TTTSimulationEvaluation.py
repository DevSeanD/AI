#!/usr/bin/python
"""
Author: Sean Dever
Date: 3/31/2021
Description: This program will serve as an example implementation of the Monte Carlo Tree Search using tic tac toe as our goal.
References:
    https://pythonguides.com/python-print-2-decimal-places/
    https://www.calculatorsoup.com/calculators/games/odds.php
"""
import random # used for random player
import os
import sys

class TTTBoard:
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.board = [['-'] * cols for row in range(rows)] # zero is the defualt space value

    def loadBoardState(self,fileName):
        moveCount = 0
        if(os.path.exists(fileName)):
            with open(fileName,"r") as gameState:
                row = 0
                moveCount = 0
                for line in gameState:
                    col = 0
                    for char in line:
                        if char == "X" or char == "O":
                            moveCount += 1
                            val = self.makeMove(row,col,char)
                            if val == 0:
                                print("Error Move not made")
                                print(row,col,char)
                        col += 1
                    row += 1;
        return moveCount

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


def playTTTGame(gameFile):
    PLAYER1ICON = "X"
    PLAYER2ICON = "O"

    game = TTTBoard(3,3)
    gameLoop = True
    #moveCount = 1
    moveCount = game.loadBoardState(gameFile) - 1 # loadBoardState returns the number of modes already made
    # game.printBoard()

    while(True):
        # Random Player Move
        player1Row, player1Col = randomPlayerMove()

        validMove = game.makeMove(player1Row,player1Col,PLAYER1ICON) # Make Player 1 Move
        while(validMove == 0):
            player1Row, player1Col = randomPlayerMove()
            validMove = game.makeMove(player1Row,player1Col,PLAYER1ICON)

        moveCount += 1
        #game.printBoard() # print state of gameboard after player1's move
        if(moveCount >= 8):
            return "NA"
        if(moveCount >= 5 and game.checkWin(PLAYER1ICON) == "X"): # Check to see if x has one
            return "X"

        player2Row, player2Col = randomPlayerMove()
        validMove = game.makeMove(player2Row,player2Col,PLAYER2ICON)

        while(validMove == 0):
            player2Row, player2Col = randomPlayerMove()

            validMove = game.makeMove(player2Row,player2Col,PLAYER2ICON)

        moveCount += 1
        if(moveCount >= 8):
            return "NA"
        if(moveCount >= 6 and game.checkWin(PLAYER2ICON) == "O"):
            return "O"

# Entry Point
if(len(sys.argv) == 2):
    xWins = 0
    oWins = 0
    simNum = 10000 # number of simulations to perform
    initState = TTTBoard(3,3)
    initState.loadBoardState(sys.argv[1])
    print()
    print("Simulating",simNum, "games from state:")
    initState.printBoard()
    print()

    for sim in range(simNum):
        result = playTTTGame(sys.argv[1])
        if(result == "X"): # X has won
            xWins += 1
        if(result == "O"): # O has won
            oWins += 1
        if(result == "NA"): # Neither player has won
            pass

    print(xWins,oWins)

    if(xWins > oWins):
        print()
        print("X has a change of: ", str("{:.2f}".format(xWins/(xWins + oWins) * 100)) + "% to win") # using the equation P_w = A / (A + B) * 100 for calculating chance of a win
    if(oWins > xWins):
        print()
        print("O has a change of: ", str("{:.2f}".format(oWins/(oWins + xWins) * 100)) + "% to win") # using the equation P_w = A / (A + B) * 100 for calculating chance of a win

else:
    print("Improper amount of argument")
    print("Ex. TTTSimulationEvaluation.py {GameState.txt}")
