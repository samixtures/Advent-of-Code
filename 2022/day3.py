#DAY 3 PART 1
# vJrwpWtwJgWrhcsFMMfFFhFp len = 24, so 1st and second compart len = 12
# first compartment: vJrwpWtwJgWr second compartment: hcsFMMfFFhFp 

"""
First thing I'll do is make sure I can determine the letter that's the same in
both compartments for the string above.
"""

# s = "vJrwpWtwJgWrhcsFMMfFFhFp"
# s = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
# s = "PmmdzqPrVvPwwTWBwg"
# s = "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"

"""
Create set with all the values in the 1st half, then loop through second half and see
if there's any value that's the same in the second half.
After getting the value I should get the numeric value associated with it.
..... it doesn't look easy to mess with the ascii values to the get numeric values.
Eh actually I can create use a loop and the ascii values to make a decent
map of size 56 I think...?

Actually from the way the ascii values are we'll just do if int(ord(s[i])) > 90: total += ascii val - 96
else total += ascii val - 38

Test case ascii vals:
In the above example, the priority of the item type that appears in both compartments of 
each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

"""


# setVals = set()
# total = 0
# for i in range(len(s)//2):
#     setVals.add(s[i])
# for i in range(len(s)//2, len(s)):
#     if s[i] in setVals:
#         # print("common value is", s[i])
#         asciiVal = int(ord(s[i]))
#         # print("the ascii value is", asciiVal)
#         if asciiVal > 90:
#             # print("ascii val is now", asciiVal - 96)
#             total += asciiVal
#         elif asciiVal <= 90:
#             # print("ascii val is now", asciiVal - 38)
#             total += asciiVal

"""
Now let's do that will all of the lines of the input file
"""
res = 0
with open('data3.txt') as file:
    for s in file:
        setVals = set()
        total = 0
        for i in range(len(s)//2):
            setVals.add(s[i])
        for i in range(len(s)//2, len(s)):
            if s[i] in setVals:
                print("common value is", s[i])
                asciiVal = int(ord(s[i]))
                print("ascii val is", asciiVal)
                # print("the ascii value is", asciiVal)
                if asciiVal > 90:
                    # print("ascii val is now", asciiVal - 96)
                    total += asciiVal - 96
                elif asciiVal <= 90:
                    # print("ascii val is now", asciiVal - 38)
                    total += asciiVal - 38
                break
        res += total
print("result is", res)