from heapq import heappop, heappush


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        st = (0, 0)
        en = (70, 70)
        points = set()
        stop = 1023
        for i, line in enumerate(fptr):
            points.add(tuple(map(int, list(eval(line)))))
        DIR = {'E': (0, 1),
               'W': (0, -1),
               'N': (-1, 0),
               'S': (1, 0)}

        st, en = 0, len(point)-1

        line = fptr.readline().strip()
        while line:
            k, l = tuple(map(int, list(eval(line))))
            points.add((k, l))
            line = fptr.readline().strip()
            heap = [[0, st]]
            vis = set()
            while heap:
                cost, loc = heappop(heap)
                if loc in vis:
                    continue
                else:
                    vis.add(loc)
                if loc == en: break
                for direct in DIR:
                    x, y = loc[0] + DIR[direct][0], loc[1] + DIR[direct][1]
                    if 0 <= x <= en[0] and 0 <= y <= en[1] and (x, y) not in points:
                        c = cost + 1
                        heappush(heap, [c, (x, y)])
            else:
                print((k, l))
                break

