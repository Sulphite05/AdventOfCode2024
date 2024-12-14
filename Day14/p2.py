import re
from collections import defaultdict

DIR = [0, 1, 0, -1, 0]


def dfs(i, j, w, h, vis, tot, area):
    if 0 <= i < w and 0 <= j < h and (i, j) not in vis:
        vis.add((i, j))
        tot[0] += area[(i, j)]
        for k in range(4):
            r, c = i + DIR[k], j + DIR[k + 1]
            if (r, c) in area:
                dfs(r, c, w, h, vis, tot, area)


def solve():
    with open('input.txt', 'r') as fptr:
        pos = []
        vel = []
        for line in fptr:
            a, b = re.findall('[0-9]+', line)[:2]
            get = re.findall('[0-9]+|-[0-9]+', line)
            x = get[-2]
            y = get[-1]
            pos.append([int(a), int(b)])
            vel.append((int(x), int(y)))

    w, h, n = 101, 103, 0

    for n in range(10000):
        area = defaultdict(int)
        for i in range(len(pos)):
            a, b = pos[i][0], pos[i][1]
            x, y = vel[i][0], vel[i][1]
            a = (a + x) % w
            b = (b + y) % h
            pos[i][0], pos[i][1] = a, b
            area[(a, b)] += 1

        vis = set()
        for i, j in area:
            if (i, j) not in vis:
                tot = [0]
                dfs(i, j, w, h, vis, tot, area)
                if tot[0] > 100: break
        else: continue
        break

    return n + 1, pos, w, h


if __name__ == '__main__':
    ans, _, _, _ = solve()
    print(ans)
