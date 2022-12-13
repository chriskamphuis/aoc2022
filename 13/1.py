import json

pairs = [(json.loads(left), json.loads(right)) for left, right in
         [pair.split('\n') for pair in open('input.txt').read().strip().split('\n\n')]]


def compare(pair):
    match pair:
        case ([x, *x2], [y, *y2]) if isinstance(x, int) and isinstance(y, int) and x < y:
            return True
        case ([x, *x2], [y, *y2]) if isinstance(x, int) and isinstance(y, int) and x > y:
            return False
        case ([x, *x2], [y, *y2]) if isinstance(x, int) and isinstance(y, int) and x == y:
            return compare((x2, y2))
        case ([x, *x2], [y, *y2]) if isinstance(x, list) and isinstance(y, list) and len(x) == 0 and len(y) > 0:
            return True
        case ([x, *x2], [y, *y2]) if isinstance(x, list) and isinstance(y, list) and len(x) > 0 and len(y) == 0:
            return False
        case ([x, *x2], [y, *y2]) if isinstance(x, list) and isinstance(y, list) and len(x) == 0 and len(y) == 0:
            return compare((x2, y2))
        case ([x, *x2], [y, *y2]) if (isinstance(x, list) and isinstance(y, list) and
                                      len(x) > 0 and len(y) > 0 and compare((x, y)) == -1):
            return compare((x2, y2))
        case ([x, *x2], [y, *y2]) if isinstance(x, list) and isinstance(y, list) and len(x) > 0 and len(y) > 0:
            return compare((x, y))
        case ([x, *x2], [y, *y2]) if isinstance(x, int) and isinstance(y, list):
            return compare(([[x], x2], [y, y2]))
        case ([x, *x2], [y, *y2]) if isinstance(x, list) and isinstance(y, int):
            return compare(([x, x2], [[y], y2]))
        case ([], []):
            return -1
        case ([], [y, *y2]):
            return True
        case ([x, *x2], []):
            return False
        case ([x], [y]):
            return compare((x, y))


print(sum([i for i, pair in enumerate(pairs, start=1) if compare(pair)]))
