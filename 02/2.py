score = 0
with open('input.txt', 'r') as f:
    for line in f:
        o, y = line.strip().split(' ')
        mp = {'A': 0, 'B': 1, 'C': 2, 'X': -1, 'Y': 0, 'Z': 1}  
        back = {0: 'X', 1: 'Y', 2: 'Z'} 
        score += (mp[y]+1) * 3 + (mp[back[(mp[o]+mp[y])%3]]+1) + 1
print(score)
