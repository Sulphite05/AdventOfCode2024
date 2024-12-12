DIR = [0, 1, 0, -1, 0]


def dfs(i, j):
    if 0 <= i < ROW and 0 <= j < COL and (i, j) not in vis:
        vis.add((i, j))
        plant = fence[i][j]
        measures[0] += 1
        ans = 0
        for k in range(4):
            r, c = i + DIR[k], j + DIR[k+1]
            if 0 <= r < ROW and 0 <= c < COL:
                if fence[r][c] != plant:
                    ans += 1
                else: dfs(r, c)
            else:
                ans += 1
        measures[1] += ans


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        fence = []
        for line in fptr:
            fence.append(list(line.strip()))

    vis = set()
    ROW, COL = len(fence), len(fence[0])
    ans = 0
    for i in range(ROW):
        for j in range(COL):
            if (i, j) not in vis:
                measures = [0, 0]
                dfs(i, j)
                ans += measures[0] * measures[1]
    print(ans)
