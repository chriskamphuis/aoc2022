lines = [[tuple(int(p) for p in point.split(',')) for point in line.strip().split(' -> ')]
         for line in open('input.txt').readlines()]
lines = [[(point[0], point[1]) for point in line] for line in lines]
sand_start = (500, 0)
max_x = max(max(point[0] for point in line) for line in lines) * 2
max_y = max(max(point[1] for point in line) for line in lines)

grid = [['.' for _ in range(max_x+2)] for _ in range(max_y+3)]

for line in lines:
    for p1, p2 in zip(line, line[1:]):
        if p1[0] == p2[0]:
            if p1[1] < p2[1]:
                for y in range(p1[1], p2[1]+1):
                    grid[y][p1[0]] = '#'
            else:
                for y in range(p2[1], p1[1]+1):
                    grid[y][p1[0]] = '#'
        else:
            if p1[0] < p2[0]:
                for x in range(p1[0], p2[0]+1):
                    grid[p1[1]][x] = '#'
            else:
                for x in range(p2[0], p1[0]+1):
                    grid[p1[1]][x] = '#'

grid[-1] = ['#' for _ in range(max_x+2)]

# start dropping sand
grid[sand_start[1]][sand_start[0]] = '+'
while True:
    # drop sand
    sand = sand_start
    while True:
        if grid[sand[1]+1][sand[0]] == '.':
            sand = (sand[0], sand[1]+1)
        elif grid[sand[1]+1][sand[0]-1] == '.':
            sand = (sand[0]-1, sand[1]+1)
        elif grid[sand[1]+1][sand[0]+1] == '.':
            sand = (sand[0]+1, sand[1]+1)
        else:
            grid[sand[1]][sand[0]] = 'o'
            break
    if sand[1] == sand_start[1] and sand[0] == sand_start[0]:
        break

print(sum(sum(1 for x in row if x == 'o') for row in grid))
