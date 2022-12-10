# DAY 4 PART 1

# 33-62,26-62 range2 in range1 so True
# 49-89,49-88 range2 in range1 so True
# 2-4,3-92    False
# 7-98,7-98   range1 in range 2 and vice versa so True

with open('data4.txt') as file:
    for line in file:
        num1, num2, num3, num4 = None, None, None, None
        dashFound = False
        counter = 0
        for x in range(len(line)):
            if line[x] == "-" and counter == 0:
                counter += 1
                num1 = int(line[0:x])
                print(num1)