print(sum(sorted([sum([int(n) for n in l.strip().split('\n')]) for l in open('input.txt').read().split('\n\n')])[-3:]))
