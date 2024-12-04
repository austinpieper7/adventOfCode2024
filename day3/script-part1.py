import re

solution = 0
#open file
with open(r'day3\input.txt', 'r') as entries:
	lines = entries.readlines()

def parseMul(mul):
    if mul is not None:
        matches = re.findall(r"\b\d{1,3}\b", mul)
        if len(matches) == 2:
            return int(matches[0]) * int(matches[1])
        else:
            print("Incorrect number of matches found....ignoring entry")
    return 0

#construct mulList
for line in lines:
    matches = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", line)
    for match in matches:
        solution += parseMul(match)

#return solution
print('solution : ' + str(solution))