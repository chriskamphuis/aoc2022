import json
from functools import cmp_to_key

pairs = [(json.loads(left), json.loads(right)) for left, right in
         [pair.split('\n') for pair in open('input.txt').read().strip().split('\n\n')]]
pairs = list(sum(pairs, ()))
pairs.append([[2]])
pairs.append([[6]])

def compare(pair):
    match pair:
        case ([x, *x2], [y, *y2]) if isinstance(x, int) and isinstance(y, int) and x < y:
            return -1
        case ([x, *x2], [y, *y2]) if isinstance(x, int) and isinstance(y, int) and x > y:
            return 1
        case ([x, *x2], [y, *y2]) if isinstance(x, int) and isinstance(y, int) and x == y:
            return compare((x2, y2))
        case ([x, *x2], [y, *y2]) if isinstance(x, list) and isinstance(y, list) and len(x) == 0 and len(y) > 0:
            return -1
        case ([x, *x2], [y, *y2]) if isinstance(x, list) and isinstance(y, list) and len(x) > 0 and len(y) == 0:
            return 1
        case ([x, *x2], [y, *y2]) if isinstance(x, list) and isinstance(y, list) and len(x) == 0 and len(y) == 0:
            return compare((x2, y2))
        case ([x, *x2], [y, *y2]) if (isinstance(x, list) and isinstance(y, list) and
                                      len(x) > 0 and len(y) > 0 and compare((x, y)) == 0):
            return compare((x2, y2))
        case ([x, *x2], [y, *y2]) if isinstance(x, list) and isinstance(y, list) and len(x) > 0 and len(y) > 0:
            return compare((x, y))
        case ([x, *x2], [y, *y2]) if isinstance(x, int) and isinstance(y, list):
            return compare(([[x], x2], [y, y2]))
        case ([x, *x2], [y, *y2]) if isinstance(x, list) and isinstance(y, int):
            return compare(([x, x2], [[y], y2]))
        case ([], []):
            return 0
        case ([], [y, *y2]):
            return -1
        case ([x, *x2], []):
            return 1
        case ([x], [y]):
            return compare((x, y))


pairs = sorted(pairs, key=cmp_to_key(lambda x, y: compare((x, y))))
decoder = 1
for i, pair in enumerate(pairs, start=1):
    if pair == [[2]]:
        decoder *= i
    if pair == [[6]]:
        decoder *= i
print(decoder)
