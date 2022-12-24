# DAY 7 PART 1
class Node:
    def __init__(self, val=0, children=[]):
        self.val = val # this is a number (integer probably)
        self.children = children # this is a list

"""
            (/)
            /  \
           (a)  (d)
           /
           (e)
"""

def helper(root):
    sum = 0
    if root.children:
        for x in root.children:
            sum += helper(x)
    return root.val + sum

def dfs(root):
    sum = 0
    size = helper(root)
    # ^ the actual size of a node with all the contents of its folders
    if size <= 10:
        sum += size
    for x in root.children:
        sum += dfs(x)
    return sum

test = Node(40, [Node(5, [Node(4)]), Node(2)])

print(helper(test)) # prints 11 as expected
print(dfs(test)) # prints 15 as expected (double counts e)



"""
/.val = 40
/.children = [a, d]

a.val = 5
a.children = [e]

d.val = 2

e.val = 4


So the value of each node is DOES NOT include the size of
    the nested folders inside the folder that represents the node.
So ^ answers the question underneath.
QUESTION: why can't we just go through every node and add up
    all of the nodes with a value of less than or equal to 100,000
    
Visit node. If its value is less than 100,000: return that value
    plus the values of all of its children and their children

dfs: goes through each node
helper func: gets the value of the node, and the value
    of its children.

"""