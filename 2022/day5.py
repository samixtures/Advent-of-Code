#DAY 5 PART 1
# Reading columns from a text file
# https://stackoverflow.com/questions/30216573/reading-specific-columns-from-a-text-file-in-python

with open('data5.1.txt') as file:
    s = "DTWNL HPC JMGDNHPW LQTNSWC NCHP BQWMDNHT LSGJRBM TRBVGWNZ LPNDGW"
    for x in s:
        result = s.split(" ")
        
    # Python code to convert string into list
    def extractDigits(lst):
        return [[el] for el in lst]       

    result = extractDigits(result)

    # Python code to convert string to list character-wise
    
    def Convert(string):
        list1 = []
        list1[:0] = string
        return list1
    
    
    # Driver code
    str1 = "ABCD"
    print(Convert(str1))

    print(result)
    num1, num2, num3 = 6, 6, 5
    print(result[5][0])
    # for i in range(num1):
    #     temp = result[num2-1].pop(0)
    #     result[num3-1].append(temp)
    # print(result)
# PHCNBQWMDN backwards

    for line in file:
            num1, num2, num3 = None, None, None
            for x in range(len(line)):
                if line[x] not in ['\n', '\r']:
                    if line[x] == "f":
                        num1 = int(line[5:x])
                        # print("num1 is", num1)
                    if line[x] == "t":
                        num2 = int(line[x-2])
                        # print("num2 is", num2)
                    if x == len(line)-2 and line[x] != " ":
                        num3 = int(line[x])
                        # print("num3 is", num3)
                    elif x == len(line)-1:
                        num3 = int(line[x])
                        # print("num3 is", num3)
            # move num1 from num2 to num3
            # where num1 is how many crates will be moved
            # num2 is which crate we are moving from
            # num3 is which crate we are moving them to
