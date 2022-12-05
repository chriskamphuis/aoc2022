import re

pairs = 0
with open('input.txt', 'r') as f:
    for line in f:
        s1, s2, e1, e2 = [int(e) for e in re.search(r"([\d]*)-([\d]*),([\d]*)-([\d]*)", line.strip()).groups()]
        if s1 >= e1 and s2 <= e2 or e1 >= s1 and e2 <= s2: 
            pairs += 1
print(pairs)
