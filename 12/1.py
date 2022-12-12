from queue import Queue

grid = []
with open('input.txt') as f:
    for y, row in enumerate(f):
        grid.append([])
        for x, column in enumerate(row.strip()):
            if column == 'S':
                start = (x, y)
                grid[y].append(0)
            elif column == 'E':
                end = (x, y)
                grid[y].append(25)
            else:
                grid[y].append(ord(column) - 97)

to_visit = Queue()
to_visit.put((start, 0))
visited = set()
while not to_visit.empty():
    (x, y), dist = to_visit.get()
    if (x, y) == end:
        print(dist)
        break
    if (x, y) in visited:
        continue
    visited.add((x, y))
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid):
            if grid[y+dy][x+dx] <= grid[y][x] + 1:
                to_visit.put(((x + dx, y + dy), dist+1))