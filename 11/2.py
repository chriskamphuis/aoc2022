class Monkey:

    def __init__(self, starting_items, instruction, test_value, if_true, if_false):
        self.items = starting_items
        self.operation = self.create_operation(instruction)
        self.test = test_value
        self.to = [if_false, if_true]

    def create_operation(self, instruction):
        match instruction.split():
            case ['old', '*', 'old']:
                return lambda old: old**2
            case ['old', '+', 'old']:
                return lambda old: 2*old
            case ['old', '*', x]:
                return lambda old: old * int(x)
            case ['old', '+', x]:
                return lambda old: old + int(x)


monkeys = []
for monkey in open('input.txt').read().split('\n\n'):
    identifier, items, operation, test, if_true, if_false = monkey.strip().split('\n')
    items = [int(item) for item in items[18:].split(', ')]
    operation = operation[19:]
    test = int(test[-2:].strip())
    if_true, if_false = [int(e[-1]) for e in [if_true, if_false]]
    monkeys.append(Monkey(items, operation, test, if_true, if_false))


monkey_counter = [0 for _ in range(len(monkeys))]
all_tests = 1
for m in monkeys:
    all_tests *= m.test

for _ in range(10000):
    for i, monkey in enumerate(monkeys):
        for item in monkey.items:
            monkey_counter[i] += 1
            worry = monkey.operation(item)
            worry %= all_tests
            monkeys[monkey.to[worry % monkey.test == 0]].items.append(worry)
        monkey.items = []
monkey_counter = sorted(monkey_counter)
print(monkey_counter[-1] * monkey_counter[-2])