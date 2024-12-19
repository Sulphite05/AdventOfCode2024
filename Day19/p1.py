
def dfs(p_ind):
    if p_ind == len(p): return True
    for j in range(p_ind+1, len(p)+1):
        if p[p_ind:j] in seq:
            if dfs(j): return True
    return False


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        seq = set(fptr.readline().strip().split(', '))
        fptr.readline()
        pat = []
        for line in fptr:
            pat.append(line.strip())

    ans = 0
    for p in pat:
        get = dfs(0)
        if get: ans += 1
    print(ans)
