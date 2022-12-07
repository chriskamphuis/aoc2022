from collections import deque

items, instructions = open('input.txt').read().split('\n\n')
stacks = [deque() for _ in range(9)]

for line in items.split('\n')[:-1][::-1]:
    for i, value in enumerate(line[1::4]):
        if value.strip():
            stacks[i].append(value)

for instruction in instructions.split('\n')[:-1]:
    ins = [e for e in instruction.split(' ')]
    m, f, t = int(ins[1]), int(ins[3])-1, int(ins[5])-1
    for _ in range(m):
        stacks[t].append(stacks[f].pop())

print("".join(s.pop() for s in stacks))
