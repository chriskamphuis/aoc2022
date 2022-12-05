priorities = {}
for i in range(97, 97+26):
    priorities[chr(i)] = i - 96
for i in range(65, 65+26):
    priorities[chr(i)] = i - 64 + 26

score = 0 
with open('input.txt') as f:
    for line in f:
        store = set()
        l = line.strip()
        for c in l[:len(l)//2]:
            store.add(c)
        for c in l[len(l)//2:]:
            if c in store:
                score += priorities[c]
                break
print(score)
