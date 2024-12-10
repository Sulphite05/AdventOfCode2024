
def dfs(curr, a, b):
    if 0 <= a < r and 0 <= b < c and mapp[a][b] == curr + 1:
        if mapp[a][b] == 9 and (a, b) not in vis: vis.add((a, b))
        else:
            for i in range(4): dfs(curr + 1, a + dirs[i], b + dirs[i + 1])


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        mapp = []
        zeroes = []
        for i, line in enumerate(fptr):
            lst = []
            for j, char in enumerate(line):
                if char!='\n': lst.append(int(char))
                if char == '0': zeroes.append((i, j))
            mapp.append(lst)

    r, c = len(mapp), len(mapp[0])
    dirs = [0, 1, 0, -1, 0]
    ans = 0
    for a, b in zeroes:
        vis = set()
        for i in range(4): dfs(0, a + dirs[i], b + dirs[i + 1])
        ans += len(vis)
    print(ans)

