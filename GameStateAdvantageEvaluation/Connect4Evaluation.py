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
        # This function returns win values based on black being the primary player. So when black loses a small number is returned and when black wins a large number is returned
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
                    return 1000
                if rVertWin >= 4:
                    return -1000

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
                    return 1000
                if rHoriWin >= 4:
                    return -1000

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
                    return 1000
                if rDiagWin >= 4:
                    return -1000

def c4Eval(state): # Eval function that takes into consideration value based locations
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
    if(bTotal > rTotal):
        print("Black has the avantage of",bTotal,"to",rTotal)
    if(bTotal == rTotal):
        print("Neither player has the advantage")

    # heurisic for min-max alg from the point of view of black
    return bTotal - rTotal

def c4Eval1(state): # Eval function that takes into consideration both value locations and opportunities to win
    evalTable = [[3,4,5,7,5,4,3],[4,6,8,10,8,6,4],[5,8,11,13,11,8,5],[5,8,11,13,11,8,5],[4,6,8,10,8,6,4],[3,4,5,7,5,4,3]]

    bValTotal = 0
    rValTotal = 0

    # value based eval
    for row in range(6):
        for col in range(7):
            if state[row][col] == 'R':
                rValTotal += evalTable[row][col]
            if state[row][col] == 'B':
                bValTotal += evalTable[row][col]


    # keeps track of piece sequence totals
    bSeqTotal = 0
    rSeqTotal = 0
    # who has move peieces in a row,col,or diagonal
    bVertWin = 0 # vertical counters
    rVertWin = 0
    for col in range(7):
        for row in range(6):
            if state[row][col] == 'B':
                bVertWin += 1
            if state[row][col] == 'R':
                rVertWin += 1
            if state[row][col] == '-' or state[row][col] == 'B':
                rVertWin = 0
            if state[row][col] == '-' or state[row][col] == 'R':
                bVertWin = 0
            if bVertWin > rVertWin:
                bSeqTotal += bVertWin
            if rVertWin > bVertWin:
                rSeqTotal += rVertWin

        bHoriWin = 0 # horizontal counters
        rHoriWin = 0
        for row in range(6):
            for col in range(7):
                if state[row][col] == 'B':
                    bHoriWin += 1
                if state[row][col] == 'R':
                    rHoriWin += 1
                if state[row][col] == '-' or state[row][col] == 'B':
                    rHoriWin = 0
                if state[row][col] == '-' or state[row][col] == 'R':
                    bHoriWin = 0
                if bHoriWin > rHoriWin:
                    bSeqTotal += bHoriWin
                if rHoriWin >= bHoriWin:
                    rSeqTotal += rHoriWin

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
                if state[min(ROW, line) - j - 1][start_col + j] == 'B':
                    bDiagWin += 1
                if state[min(ROW, line) - j - 1][start_col + j] == 'R':
                    rDiagWin += 1
                if state[min(ROW, line) - j - 1][start_col + j] == '-' or state[min(ROW, line) - j - 1][start_col + j] == 'R':
                    bDiagWin = 0
                if state[min(ROW, line) - j - 1][start_col + j] == '-' or state[min(ROW, line) - j - 1][start_col + j] == 'B':
                    rDiagWin = 0
                if bDiagWin > rDiagWin:
                    bSeqTotal += bDiagWin
                if rDiagWin > bDiagWin:
                    rSeqTotal += rDiagWin

    bValTotal += bSeqTotal
    rValTotal += rSeqTotal

    if(rValTotal > bValTotal):
        print("Red has the avantage of",rValTotal,"to",bValTotal)
    if(bValTotal > rValTotal):
        print("Black has the avantage of",bValTotal,"to",rValTotal)
    if(bValTotal == rValTotal):
         print("Neither player has the advantage")

    # heuristic from the point of view of black player
    return bValTotal - rValTotal

#Entry Point
print("Welcome to Connect4 Python!")
print()
inputLoop = True
while(inputLoop == True):
    print()
    print("What would you like to do?")
    print("1. Player 1 vs Player 2")
    print("2. Evaluate Game State File")
    choice = input()
    if choice == '1' or choice == '2':
        inputLoop = False

if choice == '1':
    inputLoop = True
    print("Player vs Player mode!")
    while(inputLoop == True):
        print()
        print("Which Evaluation function would you like to use?")
        print("1. Location Based Value")
        print("2. Location Based Value and Sequence Based Value")
        evalChoice = input()
        if evalChoice == '1' or evalChoice == '2':
            inputLoop = False

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
        while(valid != True): # loops while valid input is not provided
            player1Move = int(input("Enter a Column "))
            valid = c4GameBoard.isOpen(player1Move)

        c4GameBoard.makeMove(player1Move,P1)
        c4GameBoard.printGameBoard()
        if evalChoice == '2':
            c4Eval1(c4GameBoard.gameBoard) # prints evaluation results
        if evalChoice == '1':
            c4Eval(c4GameBoard.gameBoard) # prints evaluation results
        moveCount += 1

        if(moveCount >= 7):
            result = c4GameBoard.checkWin()
            if result != None:
                if result == 1000:
                    print("Black has won")
                if result == -1000:
                    print("Red has won")
                if result == 0:
                    print("The game has ended in a tie")
                exit()
        print()
        print("Player 2's Turn")
        valid = False
        while(valid != True):
            player2Move = int(input("Enter a Column "))
            valid = c4GameBoard.isOpen(player2Move)

        c4GameBoard.makeMove(player2Move,P2)
        c4GameBoard.printGameBoard()
        if evalChoice == '2':
            c4Eval1(c4GameBoard.gameBoard) # prints evaluation results
        if evalChoice == '1':
            c4Eval(c4GameBoard.gameBoard) # prints evaluation results
        moveCount += 1

        if(moveCount >= 7):
            result = c4GameBoard.checkWin()
            if result != None:
                if result == 1000:
                    print("Black has won")
                if result == -1000:
                    print("Red has won")
                if result == 0:
                    print("The game has ended in a tie")
                exit()

if choice == '2':
    P1 = 'B' # player 1
    P2 = 'R' # player 2

    print("Game State Evalutation mode!")
    print()
    
    inputLoop = True
    while(inputLoop == True):
        print()
        print("Which Evaluation function would you like to use?")
        print("1. Location Based Value")
        print("2. Location Based Value and Sequence Based Value")
        evalChoice = input()
        if evalChoice == '1' or evalChoice == '2':
            inputLoop = False

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
    if evalChoice == '2':
        c4Eval1(c4GameBoard.gameBoard) # prints evaluation results
    if evalChoice == '1':
        c4Eval(c4GameBoard.gameBoard) # prints evaluation results

    exit()
