# DAY 1 PART 1
# Checking for empty lines:
# https://stackoverflow.com/questions/7896495/python-how-to-check-if-a-line-is-an-empty-line

"""
PROCESS:
Create a variable for the sum of a reindeer's calories
Create a variable for the current max sum

Read through the file with the data of the calories

If the current line is empty that means we have read
all of the calories for a reindeer, so we check if the sum
of their calories is the maximum amount of calories we've seen so far from reindeer
If it is, that's the new max, otherwise we keep going
We also set the sum variable to be 0 again since we'll be checking the next reindeer's calories now
We then break.

If the current line is not empty, we add the current value to the sum variable

Finally we print out the max sum variable
"""
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

# DAY1 PART 2
sumVals = 0
stack = []
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