vis = set()


def change(r, c, i, j, m, n, area):
    while 0 <= r < m and 0 <= c < n and area[r][c] != '#':
        vis.add((r, c))
        r += i
        c += j

    if r < m and c < n and area[r][c] == '#':
        r -= i
        c -= j
        stop = False
    else:
        stop = True
    return r, c, stop


def solve():
    with open('input.txt', 'r') as fptr:
        area = []
        for line in fptr:
            area.append(list(line.strip()))

    m, n = len(area), len(area[0])
    for i in range(m):
        for j in range(n):
            if area[i][j] == '^':
                r, c = i, j
                break
    row, col = r, c
    dir = [-1, 0, 1, 0]  # u r d l
    stop = False
    i, j = 0, 1
    while not stop:
        r, c, stop = change(r, c, dir[i], dir[j], m, n, area)
        i = (i + 1) % 4
        j = (j + 1) % 4

    return vis, area, row, col


if __name__ == '__main__':
    s, lst, r, c = solve()
    print(len(s))
