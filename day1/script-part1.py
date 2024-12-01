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

x = 0

#iterate through lists
while x < len(lines):
	x += 1

	stringValue1 = min(leftList)
	stringValue2 = min(rightList)

	value1 = int(stringValue1)
	value2 = int(stringValue2)

	leftList.remove(stringValue1)
	rightList.remove(stringValue2)

	solution = solution + abs(value1 - value2)

#return solution
print(solution)