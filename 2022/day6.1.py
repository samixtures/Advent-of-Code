# DAY 6 PART 2
# mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
# nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

with open("data6.txt") as file:
    for s in file:
        for x in range(len(s)):
            if x > 13:
                counter = 13
                charSet = set()
                going = True
                for y in range(counter, -1, -1):
                    if s[x-y] not in charSet:
                        charSet.add(s[x-y])
                    elif s[x-y] in charSet:
                        print("wrong number")
                        going = False
                        break
                if going == True:
                    # should print out x as the number 18 I think
                    print("The number appears to be", x+1)
                    break
        # for line in file:
        #     print(line)