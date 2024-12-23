from collections import defaultdict


def dfs(node, num):
    if node in vis_t or node in vis: return
    if num == 2:
        if par in kids[node]:
            ans[0] += 1
        return
    vis.add(node)
    for kiddo in kids[node]:
        dfs(kiddo, num+1)


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        edges = []
        kids = defaultdict(set)
        for line in fptr:
            lst = line.strip().split('-')
            kids[lst[0]].add(lst[1])
            kids[lst[1]].add(lst[0])

        ans = [0]
        vis_t = set()
        for par in kids:
            if par[0] == 't':
                vis = set()
                dfs(par, 0)
                vis_t.add(par)

        print(ans[0])
