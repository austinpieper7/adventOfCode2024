from collections import Counter
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
    rightList.append(splitVal[1].strip())

#iterate through list
for i in leftList:
	solution = solution + int(i) * rightList.count(i)

#return solution
print(solution)