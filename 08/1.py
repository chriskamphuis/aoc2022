trees = [[int(tree) for tree in line.strip()] for line in open('input.txt').readlines()]
visible = set()


for row_no, row in enumerate(trees):
    largest = -1
    for col_no, col in enumerate(row):
        if col > largest:
            visible.add((row_no, col_no))
            largest = col
    largest = -1
    for i, col in enumerate(row[::-1], 1):
        col_no = len(row) - i
        if col > largest:
            visible.add((row_no, col_no))
            largest = col

for col_no, col in enumerate([[row[i] for row in trees] for i in range(len(trees[0]))]):
    largest = -1
    for row_no, row in enumerate(col):
        if row > largest:
            visible.add((row_no, col_no))
            largest = row
    largest = -1
    for i, row in enumerate(col[::-1], 1):
        row_no = len(col) - i
        if row > largest:
            visible.add((row_no, col_no))
            largest = row

print(len(visible))
