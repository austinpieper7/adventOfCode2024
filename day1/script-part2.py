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

#sort lists
leftList.sort()
rightList.sort()

#initialize dictionary
mydict = {}

#iterate through list
for i in leftList:
    if i in mydict:
        solution = solution + int(i) * mydict[i]
    else:
        mydict[i] = rightList.count(i)
        solution = solution + int(i) * mydict[i]
    
#return solution
print(solution)