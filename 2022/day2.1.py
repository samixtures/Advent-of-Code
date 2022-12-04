# DAY 2 PART 2
total = 0
game_hash = {'X':0, 'Y':3, 'Z':6}
with open('data2.txt') as file:
    for line in file:
        if 'A' in line: #rock
            if 'X' in line: #rock v scissors -> loss
                total += game_hash['X']
                total += 3
            if 'Y' in line: #rock v rock -> tie
                total += game_hash['Y']
                total += 1
            if 'Z' in line: #rock v paper -> win
                total += game_hash['Z']
                total += 2
        if 'B' in line: #paper
            if 'X' in line: #paper v rock -> loss
                total += game_hash['X']
                total += 1
            if 'Y' in line: #paper v paper -> draw
                total += game_hash['Y']
                total += 2
            if 'Z' in line: #paper v scissors -> win
                total += game_hash['Z']
                total += 3
        if 'C' in line: #scissors
            if 'X' in line: #scissors v paper -> loss
                total += game_hash['X']
                total += 2
            if 'Y' in line: #scissors v scissors -> draw
                total += game_hash['Y']
                total += 3
            if 'Z' in line: #scissors v rock -> win
                total += game_hash['Z']
                total += 1
print("total is", total)