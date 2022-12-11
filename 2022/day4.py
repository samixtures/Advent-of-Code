# DAY 4 PART 1

# 33-62,26-62 range2 in range1 so True
# 49-89,49-88 range2 in range1 so True
# 2-4,3-92    False
# 7-98,7-98   range1 in range 2 and vice versa so True
total = 0
with open('data4.1.txt') as file:
    for line in file:
        num1, num2, num3, num4 = None, None, None, None
        dashFound = False
        counter = 0
        savedIndex = 0
        newStart = 0
        for x in range(len(line)):
            if line[x] == "-" and counter == 0:
                counter += 1
                savedIndex = x
                num1 = int(line[0:x])
                # print("num1 is", num1)
            if line[x] == "," and counter == 1:
                counter += 1
                newStart = x+1
                num2 = int(line[savedIndex+1:x])
                # print("num2 is", num2)
            if line[x] == "-" and counter == 2:
                counter += 1
                savedIndex = x
                num3 = int(line[newStart:x])
                # print("num3 is", num3)
            if x == len(line)-1 and counter == 3:
                counter += 1
                num4 = int(line[savedIndex+1:x])
                # print("num4 is", num4)
        print(num1, num2, num3, num4)
        if num1 >= num3 and num2 <= num4:
            total += 1
        elif num1 <= num3 and num2 >= num4:
            total += 1
print(total)