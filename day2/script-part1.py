solution = 0
#open file
with open(r'day2\input.txt', 'r') as entries:
	lines = entries.readlines()

#construct valueList
valueList = []
for line in lines:
    splitVal = line.split(" ")
    valueList.append(splitVal)

#iterate through lists
x = 0
while x < len(valueList):
    y = 0
    isIncreasing = False
    isFirstEntryCheck = True
    while y < len(valueList[x]) - 1:
        distance = int(valueList[x][y]) - int(valueList[x][y+1])
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
           (not isIncreasing and distance > 0)
           or 
           distance == 0
           or
           abs(distance) > 3):
            break
        else:
            if(y == len(valueList[x]) - 2):
                print('end of line - found good record')
                solution += 1
                break
            y += 1
    x += 1
    
#return solution
print(solution)