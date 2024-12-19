from functools import lru_cache


@lru_cache
def dfs(p_no, p_ind):
    if p_ind == len(p): return 1
    ans = 0
    for j in range(p_ind+1, len(p)+1):
        if p[p_ind:j] in seq:
            ans += dfs(p_no, j)
    return ans


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        seq = set(fptr.readline().strip().split(', '))
        fptr.readline()
        pat = []
        for line in fptr:
            pat.append(line.strip())

    ans = 0
    for i, p in enumerate(pat):
        get = dfs(i, 0)
        if get: ans += get
    print(ans)


