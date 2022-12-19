# DAY 6 PART 1
# bvwbjplbgvbhsrlpgdmjqwftvncz
# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
# nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

with open('data6.txt') as file:
    # s = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    # for x in range(len(s)):
    #     if x > 3:
    #         if s[x] != s[x-1] and s[x] != s[x-2] and s[x] != s[x-3]:
    #             if s[-1] != s[x-2] and s[x-1] != s[x-3]:
    #                     if s[x-2] != s[x-3]:
    #                         print("x's value is and value's before are")
    #                         print(s[x], s[x-1], s[x-2], s[x-3])
    #                         print("x is", x+1)
    #                         break
    for s in file:
        for x in range(len(s)):
            if x > 3:
                if s[x] != s[x-1] and s[x] != s[x-2] and s[x] != s[x-3]:
                    if s[x-1] != s[x-2] and s[x-1] != s[x-3]:
                            if s[x-2] != s[x-3]:
                                print("x's value is and value's before are")
                                print(s[x], s[x-1], s[x-2], s[x-3])
                                print("x is", x+1)
                                break