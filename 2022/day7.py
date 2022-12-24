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
    listFiles = False
    for line in file:

        # "listFiles" keeps track of whether the contents of
        #   "line" are part of the ls command or not
        if "$" in line:
            listFiles = False
        # if "line" is output of ls command
        #   then we add the contents to a list that's part of
        if listFiles == True:
            print("stackdir[-1] is", stackDir[-1])
            if "/" not in hash:
                hash[stackDir[-1]] = [line]
            else:
                print("hash is", hash)
                tempList = hash[stackDir[-1]]
                tempList.append("hi")
            print("this is our hash list", hash)

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