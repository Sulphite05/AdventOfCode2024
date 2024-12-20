from heapq import heappop, heappush


def dijkstra(st, en):
    heap = [[0, st]]
    vis = dict()
    best = 0
    while heap:
        cost, loc = heappop(heap)
        if loc in vis and cost >= vis[loc]:
            continue
        else:
            vis[loc] = cost

        if loc == en:
            best = cost

        c = cost + 1
        for direct in DIR:
            x, y = loc[0] + DIR[direct][0], loc[1] + DIR[direct][1]
            if 0 <= x < row and 0 <= y < col:
                if (x, y) not in walls:
                    heappush(heap, [c, (x, y)])
    return vis, best


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        st = en = (0, 0)
        walls = set()
        for i, line in enumerate(fptr):
            for j, char in enumerate(line):
                match char:
                    case '#':
                        walls.add((i, j))
                    case 'S':
                        st = (i, j)
                    case 'E':
                        en = (i, j)
        row, col = 141, 141
        DIR = {'E': (0, 1),
               'W': (0, -1),
               'N': (-1, 0),
               'S': (1, 0)}

        start_dists, orig_cost = dijkstra(st, en)
        end_dists, _ = dijkstra(en, st)
        saves = 100
        res = 0
        cheats = 2
        for i in range(row):
            for j in range(col):
                if (i, j) not in walls and (i, j) in start_dists:
                    for k in range(max(i-cheats, 0), min(i+cheats, row-1)+1):
                        for l in range(max(j-cheats, 0), min(j+cheats, col-1)+1):
                            if (k, l) not in walls and (k, l) in end_dists:
                                manhattan = abs(i-k) + abs(j-l)
                                if manhattan > cheats:
                                    continue
                                tot = start_dists[(i, j)] + manhattan + end_dists[(k, l)]
                                if tot <= orig_cost - saves:
                                    res += 1
        print(res)



