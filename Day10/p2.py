def dfs(curr, a, b, ans):
    if 0 <= a < r and 0 <= b < c and mapp[a][b] == curr + 1:
        if mapp[a][b] == 9: return ans + 1
        val = 0
        for i in range(4): val += dfs(curr + 1, a + dirs[i], b + dirs[i + 1], ans)
        return val + ans
    return ans


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
        for i in range(4): ans += dfs(0, a + dirs[i], b + dirs[i + 1], 0)

    print(ans)



