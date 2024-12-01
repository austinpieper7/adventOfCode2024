solution = 0
#open file
with open(r'day1\input.txt', 'r') as entries:
	lines = entries.readlines()

#construct lists
leftList = []
rightList = []
for line in lines:
    splitVal = line.split("   ")
    leftList.append(splitVal[0])
    rightList.append(splitVal[1])

#sort lists
leftList.sort()
rightList.sort()

#iterate through lists
x = 0
while x < len(lines):
	solution = solution + abs(int(leftList[x]) - int(rightList[x]))
	x += 1

#return solution
print(solution)