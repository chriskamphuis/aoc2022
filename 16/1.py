import re
from functools import lru_cache

to_find = r'^.*([A-Z]{2}).*=(\d+);.*ves? (.*)$'

flow_map = dict()
flow_rate = dict()

for valve in [re.findall(to_find, line) for line in open('input.txt')]:
    label, flow, flows_to = valve[0]
    flow_map[label] = flows_to.split(', ')
    if int(flow) > 0:
        flow_rate[label] = int(flow)

@lru_cache(maxsize=None)
def run_minute(location, flow, valves_open, minute):
    if minute == 30:
        return flow
    # travel to next valve
    max_if_travel = max([flow + run_minute(next_location, flow, valves_open, minute+1) for next_location in flow_map[location]])

    # or open valve
    open_valve = -1
    if location in flow_rate.keys() and location not in [valves_open[idx:idx+2] for idx, val in enumerate(valves_open) if idx%2 == 0]:
        valves_open += location
        open_valve = flow + run_minute(location, flow+flow_rate[location], valves_open, minute+1)

    return max(max_if_travel, open_valve)


start = 'AA'
print(run_minute(start, 0, '', 1))
