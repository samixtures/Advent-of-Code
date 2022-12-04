#DAY 3 PART 1
# vJrwpWtwJgWrhcsFMMfFFhFp len = 24, so 1st and second compart len = 12
# first compartment: vJrwpWtwJgWr second compartment: hcsFMMfFFhFp 

"""
First thing I'll do is make sure I can determine the letter that's the same in
both compartments for the string above.
"""

s = "vJrwpWtwJgWrhcsFMMfFFhFp"
s = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
s = "PmmdzqPrVvPwwTWBwg"
# s = "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"
firstStart = 0
secondStart = len(s)//2

"""
Create set with all the values in the 1st half, then loop through second half and see
if there's any value that's the same in the second half.
After getting the value I should get the numeric value associated with it.
..... it doesn't look easy to mess with the ascii values to the get numeric values.
Eh actually I can create use a loop and the ascii values to make a decent
map of size 56 I think...?
"""


setVals = set()
for i in range(len(s)//2):
    setVals.add(s[i])
for i in range(len(s)//2, len(s)):
    if s[i] in setVals:
        print("common value is", s[i])
        print("the ascii value is", int(ord(s[i])))

"""
Now let's do that will all of the
"""