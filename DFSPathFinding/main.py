"""
Author: Sean Dever
Date: 2-23-2021
Description: 
  
  The following program aims to solve the Pac-Man path finding problem. It uses DFS to find the optimal path to the target. 

  Currently the reTracePath function does not retrace the optimal path, it retraces the path taken by the DFS algorithm.

"""
import os.path

class Cell:
  def __init__(self,row,col,data,flag,):
    self.row = row
    self.col = col
    self.data = data
    self.flag = flag # Visited or not
    self.previous = None # None <=> Null
    self.sequence = 0 # Used for retracing path

def buildBoard(numOfRow,numOfCol):
  board = [[0] * numOfCol for i in range(numOfRow)]
  
  for r in range(numOfRow):
    for c in range(numOfCol):
      board[r][c] = Cell(r,c,0,1)
  
  return board

def fileCopyToBoard(board,numOfRow,numOfCol,fileName):
  file1 = open(fileName, 'r')
  Lines = file1.readlines()

  for r in range(numOfRow):
    for c in range(numOfCol):
      board[r][c].data = Lines[r+2][c]

def printBoard(board,numOfRow,numOfCol):
  for r in range(numOfRow):
    for c in range(numOfCol):
      print(board[r][c].data,end='\t')
    print()

def isOnBoard(tr,tc,numOfRow,numOfCol): # tr - target row, tc - target col
  if(tr >= 0 and tr <= numOfRow and tc >= 0 and tc <= numOfCol):
    return True
  else:
    return False

def isReachableCell(board,tr,tc,numOfRow,numOfCol):
  if(isOnBoard(tr,tc,numOfRow,numOfCol) and board[tr][tc].data == '0' or board[tr][tc].flag == '1' and board[tr][tc] == '3'):
    return True  
  else:
    return False

dfsCounter = 0
stopVar = 0
pathList = []

def detectNeighbors(board,row,col,numOfRow,numOfCol): # an implicit stack will be used recursively  
  global dfsCounter # Our global variable that was defined above. We must specify to python we want to acess the global instance
  global stopVar # Used to stop the implicit stack

  neighborOffSets = [[-1,0], [0,1], [1,0],[0,-1]] # only 4 neighbors are considered at a time because no diagonal moves are allow
  
  for ni in range(4): # Only 4 cells must be searched
    nr = row + neighborOffSets[ni][0]
    nc = col + neighborOffSets[ni][1]

    if(board[nr][nc].data == '3'):
      print("The Target has been located at Row: ",board[nr][nc].row," Col: ",board[nr][nc].col)
      pathList.append("Row: "+ str(board[row][col].row) + " Col: " + str(board[row][col].col)) # Add the last cell to the pathList
      
      # Everything that remains in the stack is not the path
      stopVar = 1 # stop the implicit stack from operation

    if(isReachableCell(board,nr,nc,numOfRow,numOfCol) and stopVar == 0):
      board[nr][nc].sequence = dfsCounter
      dfsCounter += 1

      if(board[nr][nc].sequence > 0 and (board[nr][nc].data != '3' and board[nr][nc].data != '2')):
        board[nr][nc].data = board[nr][nc].sequence
      
      board[nr][nc].flag = '2'
      board[nr][nc].previous = board[row][col]

      if(detectNeighbors(board,nr,nc,numOfRow,numOfCol)): # This is our implicit stack. The condition will execute when detectNeighbors(board,nr,nc,numOfRow,numOfCol) evaluates to true
        return True

  return False # This is our stop case

def reTracePath(board,numOfRow,numOfCol):
  global pathList
  counter = dfsCounter - 1

  while(counter > 0):
    for r in range(numOfRow):
      for c in range(numOfCol):
        if board[r][c].sequence == counter and board[r][c].previous != None:
          pathList.append("Row: " + str(board[r][c].previous.row) + " " + "Col: " + str(board[r][c].previous.col))
          board[r][c].data = counter
          counter -= 1


# Entry point
fileSelect = 0

while(fileSelect != "1" and fileSelect != "2" and fileSelect != "3" and fileSelect != "4"):
  print("###################################")
  print("Welcome to DFS PacMan Path Finding")
  print("###################################")
  print()
  print("Which File would you like to load?")
  print("1 - maze.txt")
  print("2 - maze2.txt")
  print("3 - testcase1.txt")
  print("4 - New File")
  print()
  fileSelect = input("Enter selection: ")

if fileSelect == "1":
  fileSelect = "maze.txt"
if fileSelect == "2":
  fileSelect = "maze2.txt"
if fileSelect == "3":
  fileSelect = "testcase1.txt"
if fileSelect == "4":
  print()
  fileSelect = input("Enter New test file name with extension: ")
  while(not(os.path.isfile(fileSelect))):
    print("! File Not Found !")
    fileSelect = input("Enter New test file name with extension: ")

# Using readlines() to store all lines into Lines
file1 = open(fileSelect, 'r')
Lines = file1.readlines()

numRow = int(Lines[0]) # First line = number of rows
numCol = int(Lines[1]) # Second line = number of cols

gameBoard = buildBoard(numRow,numCol) # generate gameBoard

fileCopyToBoard(gameBoard,numRow,numCol,fileSelect) # copy file to gameBoard

for row in range(numRow):
  for col in range(numCol):
    if gameBoard[row][col].data == '2':
      print()
      print("The Ghost has been located at Row: ", row, " Col: ",col,end=" ")
      ghost = Cell(row,col,'2',0)


print()
detectNeighbors(gameBoard,ghost.row,ghost.col,numRow,numCol) # 3,2
print()

reTracePath(gameBoard,numRow,numCol)


# The pathList must be reversed to show path from ghost to target
pathList.reverse()

printCounter = 0
print("Ghost",end=" -> ")
for edge in pathList:
  if printCounter == 3:
    printCounter = 0
    print()
  print(edge,end=' -> ')
  printCounter += 1

print("Target")
print()

printBoard(gameBoard,numRow,numCol)
