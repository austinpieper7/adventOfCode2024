solution = 0
#open file
with open(r'day2\input.txt', 'r') as entries:
	lines = entries.readlines()

#construct valueList
valueList = []
for line in lines:
    splitVal = line.split(" ")
    valueList.append(splitVal)

#checkEntry function
def checkEntry(currentEntry):
    y = 0
    isIncreasing = False
    isFirstEntryCheck = True
    foundSolution = True
    sameValueCount = 0
    jumpCount = 0
    worthIterativeCheck = True
    while y < len(currentEntry) - 1:
        distance = int(currentEntry[y].strip()) - int(currentEntry[y+1].strip())
        #if this is the first check, confirm direction
        if(isFirstEntryCheck):
            isFirstEntryCheck = False
            if(distance > 0):
                isIncreasing = True
        #check if still moving in the same direction
        #or if distance is 0
        #or if distance is out of band
        if((isIncreasing and distance < 0)
           or
           (not isIncreasing and distance > 0)):
           foundSolution = False
           y += 1
           continue
        elif(distance == 0):
           foundSolution = False
           sameValueCount += 1
           y += 1
           continue
        elif(abs(distance) > 3):
            foundSolution = False
            jumpCount += 1
            y += 1
            continue
        y += 1
    
    if(sameValueCount > 1 or jumpCount > 1):
        worthIterativeCheck = False
    return foundSolution,worthIterativeCheck

#iterate through lists
x = 0
while x < len(valueList):
    foundError = False
    foundSolution,worthIterativeCheck = checkEntry(valueList[x])
    if(foundSolution) :
        #incrementing solution - first check
        solution += 1
    elif(worthIterativeCheck):
        #no multiple jumps, but first check failed. Iterating through all elements
        y = 0
        while(y < len(valueList[x])):
            testValueList = list(valueList[x])
            testValueList.pop(y)
            foundSolution,worthIterativeCheck = checkEntry(testValueList)
            if(foundSolution):
                #incrementing solution - iterative check
                solution += 1
                break
            y += 1
    x += 1
#return solution
print('solution : ' + str(solution))