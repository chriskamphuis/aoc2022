line = open('input.txt').read().strip()
for i in range(len(line)-14):
    if len(list(set(line[i:i+14]))) == 14:
        print(i+14)
        break
