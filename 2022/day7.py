# Day 7 Part 1
"""
This one looks tough.
A hashmap seems decent here, with the key being 
    the directory name and the value being the
    sizes of the files in that directory.

Let's also create a stack to keep track of what directory we're in?
Actually this only seems good for when we cd deep
    and then we do "cd .." to move through directories
    in that fashion...
This is actually really interesting, considering
    I'm not too sure what data structure(s) I'd use
    to design a file system...

Well the main directory, the "/" directory, contains
    everything else, so within that directory maybe we can have 
    a list of everything in it.

We start off in the "/" directory, if the user does ls we add
    everything in there to the "/" list (maybe the list should
    be the value of the key "/" in a hashmap)
"""

with open("data7.txt") as file:
    slashDir = []
    hash = {}
    stackDir = []
    listFiles = "False"
    for line in file:

        # "listFile" keeps track of whether the contents of
        #   "line" are part of the ls command or not
        if "$" in line:
            listFiles = False
        # if "line" is output of ls command
        #   then we add the contents to a list that's part of
        if listFiles == True:
            if not hash[stackDir[-1]]:
                hash[stackDir[-1]] = [line]
            else:
                hash[stackDir[-1]].append(line)
            print("this is our hash list", hash[-1])

        # Below code for tracking directories
        if "$ cd .." in line:
            stackDir.pop()
        elif "$ cd" in line:
            stackDir.append(line[5])
        print("stackDir is", stackDir)
        # The above creates stack with [-1] as current directory

        if "$ ls" in line:
            print("line is", line)
            listFiles = True
        # print("listFiles is", listFiles)