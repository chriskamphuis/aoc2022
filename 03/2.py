priorities = {}
for i in range(97, 97+26):
    priorities[chr(i)] = i - 96
for i in range(65, 65+26):
    priorities[chr(i)] = i - 64 + 26

score = 0 
with open('input.txt') as f:
    while True:
        elfs = [f.readline().strip() for i in range(3)]
        if not elfs[0]:
            break
        store = {e for e in elfs[0]}
        store = {e for e in elfs[1] if e in store}
        for e in elfs[2]:
            if e in store:
                score += priorities[e]
                break
print(score)
