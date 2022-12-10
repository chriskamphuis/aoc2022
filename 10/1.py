cycle = 0
register = 1
score = 0

def increase_cycle():
    global cycle, score, register
    cycle += 1
    if (cycle + 20) % 40 == 0:
        score += cycle * register

for ins in [instruction.strip() for instruction in open('input.txt').readlines()]:
    match ins.split():
        case ['noop']:
            increase_cycle()
        case ['addx', x]:
            increase_cycle()
            increase_cycle()
            register += int(x)

print(score)