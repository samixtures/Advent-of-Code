# DAY 2 PART 1
"""
    Create a var to keep track of the sum
    Create hashmap for x, y, z with 1, 2, 3 since I'll always play one of those 3 and get that # added?
    If A in line and X in line: (rock vs rock) add 1 + 3 (rock + draw)
    If A in line and Y in line: (rock vs paper) add 2 + 6 (paper + win)
    If A in line and Z in line: (rock vs scissors) add 3 + 0 (scissors + loss)
    Same for B, and C I guess. That's 9 if statements. Is there a better way?

    if A in line:
        if X in line
        if Y in line
        if Z in line
    Same for B and C. Feels cleaner.

    Hashmap feels useful here, but what would the keys and values be?

    I can only think of this one since these are the only times the keys and values will be constant right?:
    game_hash = {'X':1, 'Y':2, 'Z':3}


"""
total = 0
game_hash = {'X':1, 'Y':2, 'Z':3}
with open('data2.txt') as file:
    for line in file:
        if 'A' in line: #rock
            if 'X' in line: #rock v rock -> draw
                total += game_hash['X']
                total += 3
            if 'Y' in line: #rock v paper -> win
                total += game_hash['Y']
                total += 6
            if 'Z' in line: #rock v scissors -> loss
                total += game_hash['Z']
                total += 0
        if 'B' in line: #paper
            if 'X' in line: #paper v rock -> loss
                total += game_hash['X']
                total += 0
            if 'Y' in line: #paper v paper -> draw
                total += game_hash['Y']
                total += 3
            if 'Z' in line: #paper v scissors -> win
                total += game_hash['Z']
                total += 6
        if 'C' in line: #scissors
            if 'X' in line: #scissors v rock -> win
                total += game_hash['X']
                total += 6
            if 'Y' in line: #scissors v paper -> loss
                total += game_hash['Y']
                total += 0
            if 'Z' in line: #scissors v scissors -> draw
                total += game_hash['Z']
                total += 3
print("total is", total)