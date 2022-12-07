line = open('input.txt').read().strip()
for i in range(len(line)-4):
    if len(list(set(line[i:i+4]))) == 4:
        print(i+4)
        break
