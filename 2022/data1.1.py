# DAY 1 PART 2# Checking for empty lines:
# https://stackoverflow.com/questions/7896495/python-how-to-check-if-a-line-is-an-empty-line

sumVals = 0
sumList = []
with open('data1.txt') as file:
    for line in file:
        if line in ['\n', '\r']:
            # print("issa empty")
            sumList.append(sumVals)
            sumVals = 0
            continue
        sumVals += int(line)
sumOf3 = 0
for x in range(3):
    sumOf3 += max(sumList)
    sumList.remove(max(sumList))
print("sum of 3 is", sumOf3)