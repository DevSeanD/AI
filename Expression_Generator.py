"""
Author: Sean Dever
File: ExpressionGenerator.py
Description: 
"""
class evaluate:
    def __init__(self,size):
        self.top = -1
        self.size = size
        self.stackArr = []

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.stackArr.pop()
    def push(self,elm):
        self.top += 1
        self.stackArr.append(elm)

    def evaluatePostFixExp(self,exp):
        for e in exp:
            if e.isdigit(): # if the char is a digit 
                self.push(e)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(str(val2) + str(e) + str(val1))))

        return float(self.pop())

def allExpressions(numList):
    expresssion = ""
    totalExpressions = []
    operators = ['+','-','*','/']
    space = ""
    # 3 operators must be chosen per expression with 4 operands
    for oper0 in range(4):
        for oper1 in range(4):
            for oper2 in range(4):
                #pattern 1 NNNNOOO
                expression = numList[0] + space + numList[1] + space + numList[2] + space +  numList[3] + space + str(operators[oper0]) + space + str(operators[oper1]) + space + str(operators[oper2])
                totalExpressions.append(expression)
                #pattern 2 NNNONOO
                expression = numList[0] + space + numList[1] + space + numList[2] + space + str(operators[oper0]) + space + numList[3] + space + str(operators[oper1]) + space + str(operators[oper2])
                totalExpressions.append(expression)

                #pattern 3 NNONNOO
                expression = numList[0] + space + numList[1] + space + str(operators[oper0]) + space + numList[2] + space + numList[3] + space + str(operators[oper1]) + space + str(operators[oper2])
                totalExpressions.append(expression)

                #pattern 4 NNNOONO
                expression = numList[0] + space + numList[1] + space + numList[2] + space + str(operators[oper0]) + space + str(operators[oper1]) + space + numList[3] + space + str(operators[oper2])
                totalExpressions.append(expression)

                #pattern 5 NNONONO
                expression = numList[0] + space + numList[1] + space + str(operators[oper0]) + space + numList[2] + space + str(operators[oper1]) + space + numList[3] + space + str(operators[oper1])
                totalExpressions.append(expression)
                
    return totalExpressions


#Entry point
print("Enter a sequence of 4 numbers to be evaluated. 0-9 with no spaces in between")
print(" ")
numSeq = input("")
allExpress = allExpressions(numSeq)

print("Enter the target sum value")
print(" ")
targetSum = input("")

#Evaluate all expressions
for exp in allExpress:
    result = evaluate(len(exp))
    if(result.evaluatePostFixExp(exp) == float(targetSum)):
        print()
        print("The value of %s is %f"%(exp,result.evaluatePostFixExp(exp))) 
