"""
Author: Sean Dever
Date: 4/14/21
Resources: https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/ -- Diagonal traversal
"""
class connect4Game:
    def __init__(self,gameBoard):
        self.gameBoard = [['-' for i in range(7)] for j in range(6)] # create 6 by 7 connect4 board

    def isOpen(self,requestCol):
        if requestCol < 7:
            if self.gameBoard[0][requestCol] == "-": # if this is false then the entire col is filled
                return True
            else:
                return False
        else:
            return False

    def makeMove(self,requestCol,playerIcon):
        if self.isOpen(requestCol): # if the column is open for pieces
            for row in range(6):
                if self.gameBoard[row][requestCol] == "-":
                    lowestRow = row

            self.gameBoard[lowestRow][requestCol] = playerIcon
        else:
            print("Invalid Move")

    def printGameBoard(self):
        for row in range(6):
            for col in range(7):
                print(self.gameBoard[row][col],end='\t')
            print()

    def checkWin(self):
        bVertWin = 0 # vertical counters
        rVertWin = 0
        for col in range(7):
            for row in range(6):
                if self.gameBoard[row][col] == 'B':
                    bVertWin += 1
                if self.gameBoard[row][col] == 'R':
                    rVertWin += 1
                if self.gameBoard[row][col] == '-' or self.gameBoard[row][col] == 'B':
                    rVertWin = 0
                if self.gameBoard[row][col] == '-' or self.gameBoard[row][col] == 'R':
                    bVertWin = 0
                if bVertWin >= 4:
                    return("Black has won!")
                if rVertWin >= 4:
                    return("Red has won!")

        bHoriWin = 0 # horizontal counters
        rHoriWin = 0
        for row in range(6):
            for col in range(7):
                if self.gameBoard[row][col] == 'B':
                    bHoriWin += 1
                if self.gameBoard[row][col] == 'R':
                    rHoriWin += 1
                if self.gameBoard[row][col] == '-' or self.gameBoard[row][col] == 'B':
                    rHoriWin = 0
                if self.gameBoard[row][col] == '-' or self.gameBoard[row][col] == 'R':
                    bHoriWin = 0
                if bHoriWin >= 4:
                    return("Black has won!")
                if rHoriWin >= 4:
                    return("Red has won!")

        bDiagWin = 0 # diagonal counters
        rDiagWin = 0
        ROW = 6
        COL = 7
        # There will be 6 + 7 -1 lines in the output
        # 6 rows 7 cols
        for line in range(1,(ROW + COL)):
            # Get column index of the first element
            # in this line of output. The index is 0
            # for first ROW lines and line - ROW for
            # remaining lines
            start_col = max(0,line - ROW)
            # Get count of elements in this line.
            # The count of elements is equal to minimum of line number, COL-start_col and ROW
            count = min(line,(COL - start_col),ROW)
            # Print elements of this line
            for j in range(0, count):
                if self.gameBoard[min(ROW, line) - j - 1][start_col + j] == 'B':
                    bDiagWin += 1
                if self.gameBoard[min(ROW, line) - j - 1][start_col + j] == 'R':
                    rDiagWin += 1
                if self.gameBoard[min(ROW, line) - j - 1][start_col + j] == '-' or self.gameBoard[min(ROW, line) - j - 1][start_col + j] == 'R':
                    bDiagWin = 0
                if self.gameBoard[min(ROW, line) - j - 1][start_col + j] == '-' or self.gameBoard[min(ROW, line) - j - 1][start_col + j] == 'B':
                    rDiagWin = 0
                if bDiagWin >= 4:
                    return("Black has won!")
                if rDiagWin >= 4:
                    return("Red has won!")


def c4Eval(state):
    # value of each space
    evalTable = [[3,4,5,7,5,4,3],[4,6,8,10,8,6,4],[5,8,11,13,11,8,5],[5,8,11,13,11,8,5],[4,6,8,10,8,6,4],[3,4,5,7,5,4,3]]

    bTotal = 0
    rTotal = 0

    for row in range(6):
        for col in range(7):
            if state[row][col] == 'R':
                rTotal += evalTable[row][col]
            if state[row][col] == 'B':
                bTotal += evalTable[row][col]
    
    if(rTotal > bTotal):
        print("Red has the avantage of",rTotal,"to",bTotal)
        return -1000
    if(bTotal > rTotal):
        print("Black has the avantage of",bTotal,"to",rTotal)
        return 1000
    if(bTotal == rTotal):
        print("Neither player has the advantage")
        return 0
    
    # return rTotal - bTotal

#Entry Point
print("Welcome to Connect4 Python!")
print()
print("What would you like to do?")
print("1 Player 1 vs Player 2")
print("2 Evaluate Game State File")
choice = input()

if choice == '1':
    print("Player vs Player mode!")
    print()

    P1 = 'B' # player 1
    P2 = 'R' # player 2
    moveCount = 0
    board = []
    c4GameBoard = connect4Game(board)
    c4GameBoard.printGameBoard()

    while(True): # game game loop
        print()
        print("Player 1's Turn")
        valid = False
        while(valid != True): # loops while a valid input is not provided
            player1Move = int(input("Enter a Column "))
            valid = c4GameBoard.isOpen(player1Move)

        c4GameBoard.makeMove(player1Move,P1)
        c4GameBoard.printGameBoard()
        c4Eval(c4GameBoard.gameBoard) # prints evaluation results
        moveCount += 1

        if(moveCount >= 8):
            result = c4GameBoard.checkWin()
            if result != None:
                print(result)
                exit()
        print()
        print("Player 2's Turn")
        valid = False
        while(valid != True):
            player2Move = int(input("Enter a Column "))
            valid = c4GameBoard.isOpen(player2Move)

        c4GameBoard.makeMove(player2Move,P2)
        c4GameBoard.printGameBoard()
        c4Eval(c4GameBoard.gameBoard) # prints evaluation results
        moveCount += 1

        if(moveCount >= 8):
            result = c4GameBoard.checkWin()
            if result != None:
                print(result)
                exit()

if choice == '2':
    P1 = 'B' # player 1
    P2 = 'R' # player 2

    print("Game State Evalutation mode!")
    print()
    fileName = input("What is the file name? ")

    board = []
    c4GameBoard = connect4Game(board)

    c4State = open(fileName, 'r')
    state = c4State.readline()

    playerMove = True; # true for player1 false for player2
    for move in state:
        if(playerMove == True and move != ' ' and move != '\n'):
            c4GameBoard.makeMove(int(move),P1)
        if(playerMove == False and move != ' ' and move != '\n'):
            c4GameBoard.makeMove(int(move),P2)
        if(move != ' '):
            playerMove = not playerMove # change turn

    c4GameBoard.printGameBoard()
    c4Eval(c4GameBoard.gameBoard) # prints evaluation results
    exit()
