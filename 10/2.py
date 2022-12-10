cycle = 0
register = 1
drawn = ['', '', '', '', '', '']

def increase_cycle():
    global cycle, register, drawn
    if abs(register - cycle % 40) < 2:
        drawn[cycle//40]+='#'
    else:
        drawn[cycle//40]+=' '
    cycle += 1

for ins in [instruction.strip() for instruction in open('input.txt').readlines()]:
    match ins.split():
        case ['noop']:
            increase_cycle()
        case ['addx', x]:
            increase_cycle()
            increase_cycle()
            register += int(x)

[print(d) for d in drawn]