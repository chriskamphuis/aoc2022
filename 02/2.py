score = 0
with open('input.txt', 'r') as f:
    for line in f:
        o, y = line.strip().split(' ')
        if y == 'Z':
            score += 6
        if y == 'Y':
            score += 3
        forw = {'A': 0, 'B': 1, 'C': 2}  
        diff = {'X': -1, 'Y': 0, 'Z': 1}
        back = {0: 'X', 1: 'Y', 2: 'Z'} 
        s = back[(forw[o]+diff[y])%3]
        if s == 'X':
            score += 1
        if s == 'Y':
            score += 2
        if s == 'Z': 
            score += 3
print(score)
