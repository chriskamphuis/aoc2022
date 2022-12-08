trees = [[int(tree) for tree in line.strip()] for line in open('input.txt').readlines()]
max_scenic_score = -1

for row_no in range(1, len(trees)-1):
    for col_no in range(1, len(trees[0])-1):
        scenic_score = 1
        tree = trees[row_no][col_no]

        # look left
        for v, t in enumerate(trees[row_no][col_no-1::-1], 1):
            if t < tree:
                continue
            break
        scenic_score *= v

        # look right
        for v, t in enumerate(trees[row_no][col_no+1:], 1):
            if t < tree:
                continue
            break
        scenic_score *= v

        # look up
        for v, t in enumerate([t[col_no] for t in trees[:row_no]][::-1], 1):
            if t < tree:
                continue
            break
        scenic_score *= v

        # look down
        for v, t in enumerate([t[col_no] for t in trees[row_no+1:]], 1):
            if t < tree:
                continue
            break
        scenic_score *= v

        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(max_scenic_score)
