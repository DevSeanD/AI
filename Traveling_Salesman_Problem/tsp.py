import math
from itertools import permutations  

class city:
  def __init__(self,x,y,id):
    self.x = x
    self.y = y
    self.id = id
  
def calcDist(sCity,dCity): # source city and destination city
  x1 = sCity.x
  x2 = dCity.x

  y1 = sCity.y
  y2 = dCity.y

  result = math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)) # sqrt( (x2 - x1)^2 + (y2 - y1) ) 

  return result 

def generatePathList(totalCities,totalPaths): # Calculates cost from one city to every other city
  for elm in totalCities:
    for elm2 in totalCities:
      if(elm == elm2): # Skip case where the two cities are the same
        pass
      else:
        totalPaths.append(str(elm.id) + ":" + str(elm2.id) + ":" + str(calcDist(elm,elm2)))
  return totalPaths

def printPermuteList(totalPermute):
  lineCount = 0
  for perm in totalPermute: # Prints all possible paths
    print(lineCount,end=' ')
    for city in perm:
      print(city.id,end=' ')
    print()
    lineCount += 1

def printPermuteListIndex(totalPermute,index):
  lineCount = 0
  for perm in totalPermute:
    for city in perm:
      if lineCount == index:
        print(city.id,end=' ')
    lineCount += 1


# Reading data from external text file
cityList = []
externFile = open ("cities_10.txt", "r")

for line in externFile:
  #print(line[0]+line[1],end=' ') # prints city id
  #print(line[3]+line[4]+line[5],end=' ') # print city x coord
  #print(line[7]+line[8]+line[9]) 
  cityId = line[0]+line[1]
  cityX = int(line[3]+line[4]+line[5])
  cityY = int(line[7]+line[8]+line[9])
  cityObj = city(cityX,cityY,cityId)
  cityList.append(cityObj)

print("Computing Shortest path...This may take some time...")

pathList = []
permuteCityList = permutations(cityList)

generatePathList(cityList,pathList) # Should round results

pathWeight = []

for line in permuteCityList:
  sum = 0
  for city in range(len(line)):
    if(city + 1 < len(line)):
        sum += calcDist(line[city+1],line[city])
    if(city == len(line)-1):
      pathWeight.append(str(sum))

minCost = 9999999.9999
lineCount = 0
pathIndex = 0

for line in pathWeight:
  if float(line) < minCost:
    minCost = float(line)
    pathIndex = lineCount
  lineCount += 1
  
print(minCost)
print(pathIndex)

permuteCityList = permutations(cityList)
printPermuteListIndex(permuteCityList,pathIndex)
print("is the shortest path and has a weight of",minCost)
