head = (0, 0)
tails = [(0, 0) for _ in range(9)]
seen = {(0, 0)}

move = {
    'U': lambda x: (x[0], x[1]+1),
    'D': lambda x: (x[0], x[1]-1),
    'L': lambda x: (x[0]-1, x[1]),
    'R': lambda x: (x[0]+1, x[1])
}


def follow(t, h):
    if abs(t[0] - h[0]) < 2 and abs(t[1] - h[1]) < 2:
        return t
    updates = []
    if t[0] < h[0]: updates.append(move['R'])
    if t[0] > h[0]: updates.append(move['L'])
    if t[1] < h[1]: updates.append(move['U'])
    if t[1] > h[1]: updates.append(move['D'])
    for u in updates:
        t = u(t)
    return t


for action, count in [[a, int(c)] for a, c in [line.strip().split(' ') for line in open('input.txt').readlines()]]:
    for _ in range(count):
        head = move[action](head)
        tails[0] = follow(tails[0], head)
        for i in range(1, 9):
            tails[i] = follow(tails[i], tails[i-1])
        seen.add(tails[-1])
print(len(seen))