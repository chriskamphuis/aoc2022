score = 0
with open('input.txt', 'r') as f:
    for line in f:
        o, y = line.strip().split(' ')
        if o == 'A' and y == 'Y' or o == 'B' and y == 'Z' or o == 'C' and y == 'X':
            score += 6
        if o == 'A' and y == 'X' or o == 'B' and y == 'Y' or o == 'C' and y == 'Z':
            score += 3
        if y == 'X':
            score += 1
        if y == 'Y':
            score += 2
        if y == 'Z': 
            score += 3
print(score)
