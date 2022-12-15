import re

sensors_and_bacons = [tuple(int(e) for e in re.findall(r'-?\d+', line)) for line in open('input.txt')]

row_y = 2000000
no_bacons = 0
spans = []
for sx, sy, bx, by in sensors_and_bacons:
    manhattan_distance_m1 = abs(sx - bx) + abs(sy - by)
    distance_to_row = abs(sy - row_y)
    if distance_to_row > manhattan_distance_m1:
        continue
    distance_on_row = manhattan_distance_m1 - distance_to_row
    start_x, end_x = sx - distance_on_row, sx + distance_on_row
    spans += [(start_x, end_x)]
spans.sort()
new_intervals = [spans[0]]
for start_x, end_x in spans[1:]:
    if start_x <= new_intervals[-1][1]:
        new_intervals[-1] = (new_intervals[-1][0], max(new_intervals[-1][1], end_x))
for interval in new_intervals:
    no_bacons += interval[1] - interval[0]
print(no_bacons)
