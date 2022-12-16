import re

to_find = r'^.*([A-Z]{2}).*=(\d+);.*ves? (.*)$'

flow_map = dict()
flow_rate = dict()

for valve in [re.findall(to_find, line) for line in open('input.txt')]:
    label, flow, flows_to = valve[0]
    flow_map[label] = flows_to.split(', ')
    if int(flow) > 0:
        flow_rate[label] = int(flow)


# find the shortest path from every node to another node:
def shortest_path(from_node, to_node, path=[]):
    if from_node == to_node:
        return 0
    if len([next_node for next_node in flow_map[from_node] if next_node not in path]) == 0:
        return 26
    return min(
        [
           1 + shortest_path(next_node, to_node, [p for p in path] + [from_node])
           for next_node in flow_map[from_node] if next_node not in path
        ]
    )


# find length of all shortest paths for important nodes:
shortest_paths = dict()
important_keys = ['AA']
important_keys += [k for k in flow_rate.keys()]
for from_node in important_keys:
    for to_node in important_keys:
        if from_node != to_node:
            shortest_paths[(from_node, to_node)] = shortest_path(from_node, to_node)


def possible_paths(path=['AA'], minute=0, dont_allow=set()):
    if minute == 26:
        yield [p for p in path]
    elif minute > 26:
        yield [p for p in path][:-1]
    else:
        for next_node in important_keys:
            if next_node not in path and next_node not in dont_allow:
                yield from possible_paths([p for p in path] + [next_node], minute+shortest_paths[path[-1], next_node]+1, dont_allow=dont_allow)
        if len(path) == len(important_keys):
            yield [p for p in path]
        yield path


def calculate_flow(path):
    path = [path[idx:idx+2] for idx, val in enumerate(path) if idx % 2 == 0]
    flows = []
    current_pressure = 0
    distance = sum([1 + shortest_paths[(f, t)] for f, t in zip(path, path[1:])])
    for f, t in zip(path, path[1:]):
        for _ in range(shortest_paths[(f, t)]):
            flows.append(current_pressure)
        flows.append(current_pressure)
        current_pressure += flow_rate[t]
    for i in range(26 - distance):
        flows.append(current_pressure)
    return flows


list_possible_paths = list(possible_paths())
list_possible_paths = sorted(list_possible_paths, key=lambda x: sum(calculate_flow(''.join(x))), reverse=True)

# Assume player path is almost optimal, so we only search through promising paths
max_flow = 0
for p in list_possible_paths[:50]:
    f1 = calculate_flow(''.join(p))
    for e in possible_paths(dont_allow=set(p)):
        f2 = calculate_flow(''.join(e))
        if sum([a+b for a, b in zip(f1, f2)]) > max_flow:
            max_flow = sum([a+b for a, b in zip(f1, f2)])
print(max_flow)
