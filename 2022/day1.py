# DAY 1 PART 1
# Checking for empty lines:
# https://stackoverflow.com/questions/7896495/python-how-to-check-if-a-line-is-an-empty-line
sumVals = 0
maxVal = 0
with open('data1.txt') as file:
    for line in file:
        if line in ['\n', '\r']:
            print("issa empty")
            maxVal = max(sumVals, maxVal)
            sumVals = 0
            continue
        # print(int(line))
        sumVals += int(line)
print(f"The maximum amount of a calories a reindeer has is: {maxVal}!")