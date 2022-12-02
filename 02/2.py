score = 0
with open('input.txt', 'r') as f:
    for line in f:
        o, y = line.strip().split(' ')
        forw = {'A': 0, 'B': 1, 'C': 2}  
        diff = {'X': -1, 'Y': 0, 'Z': 1}
        back = {0: 'X', 1: 'Y', 2: 'Z'} 
        s = back[(forw[o]+diff[y])%3]
        score += (diff[y]+1) * 3 + (diff[s]+1) + 1
print(score)
