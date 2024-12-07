
def dfs(res, curr, ind, op):
    if ind == n: return res == curr
    if res < curr: return False
    match op:
        case '*': curr = curr*lst[ind]
        case '+': curr = curr + lst[ind]
        case '||': curr = int(str(curr)+str(lst[ind]))
    mul = dfs(res, curr, ind+1, '*')
    add = dfs(res, curr, ind+1, '+')
    concat = dfs(res, curr, ind+1, '||')
    return mul or add or concat


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        bridge = []
        for line in fptr:
            lst = line.strip().split()
            bridge.append([int(lst[0][:-1]), list(map(int, line.rstrip().split()[1:]))])
    ans = 0
    for line in bridge:
        lst = line[1]
        n = len(lst)
        get = dfs(line[0], line[1][0], 1, '+') or dfs(line[0], line[1][0], 1, '*') or dfs(line[0], line[1][0], 1, '||')
        ans += line[0] if get else 0
    print(ans)

