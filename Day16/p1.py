from heapq import heappop, heappush


def solve():
    with open('input.txt', 'r') as fptr:
        st = en = (0, 0)
        points = set()
        for i, line in enumerate(fptr):
            for j, char in enumerate(line):
                match char:
                    case '.':
                        points.add((i, j))
                    case 'S':
                        st = (i, j)
                    case 'E':
                        en = (i, j)

        points.add(en)

        DIR = {'E': (0, 1),
               'W': (0, -1),
               'N': (-1, 0),
               'S': (1, 0)}

        heap = [[0, st, 'E']]
        vis = set()
        while heap:
            cost, loc, d = heappop(heap)
            if (loc, d) in vis:
                continue
            else:
                vis.add((loc, d))
            if loc == en: break
            for direct in DIR:
                x, y = loc[0] + DIR[direct][0], loc[1] + DIR[direct][1]
                if (x, y) in points:
                    if direct == d:
                        c = cost + 1
                    elif d in 'EW' and direct in 'NS' or d in 'NS' and direct in 'EW':
                        c = cost + 1001
                    else:
                        continue
                    heappush(heap, [c, (x, y), direct])
        return cost, st, en, points


if __name__ == '__main__':
    ans, _, _, _ = solve()
    print(ans)
