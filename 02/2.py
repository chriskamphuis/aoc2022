mp = {'A': 0, 'B': 1, 'C': 2, 'X': -1, 'Y': 0, 'Z': 1, 's': 0, 0: 'X', 1: 'Y', 2: 'Z'}  
for o, y in [line.strip().split() for line in open('input.txt')]:
    mp['s'] += (mp[y]+1) * 3 + (mp[mp[(mp[o]+mp[y])%3]]+1) + 1
print(mp['s'])
