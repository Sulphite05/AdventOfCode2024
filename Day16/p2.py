from collections import defaultdict
from heapq import heappop, heappush
from p1 import solve


if __name__ == '__main__':
        t_cost, st, en, points = solve()

        DIR = {'E': (0, 1),
               'W': (0, -1),
               'N': (-1, 0),
               'S': (1, 0)}

        heap = [[0, st, 'E', None]]
        best_costs = dict()
        best_paths = defaultdict(set)

        while heap:
            cost, loc, d, prev = heappop(heap)
            if cost > t_cost:
                break
            if (loc, d) in best_paths:
                if best_costs[(loc, d)] == cost:
                    best_paths[(loc, d)].add(prev)
                continue

            best_costs[(loc, d)] = cost
            best_paths[(loc, d)].add(prev)
            prev = (loc, d)

            for direct in DIR:
                x, y = loc[0] + DIR[direct][0], loc[1] + DIR[direct][1]
                if (x, y) in points:
                    if direct == d:
                        c = cost + 1
                    elif d in 'EW' and direct in 'NS' or d in 'NS' and direct in 'EW':
                        c = cost + 1001
                    else:
                        continue
                    heappush(heap, [c, (x, y), direct, prev])

        tiles, routes = set(), set()

        def walk(curr):
            if curr and curr not in routes:
                routes.add(curr)
                tiles.add(curr[0])
                for n_curr in best_paths[curr]:
                    walk(n_curr)

        for d in DIR:
            walk((en, d))

        print(len(tiles))
