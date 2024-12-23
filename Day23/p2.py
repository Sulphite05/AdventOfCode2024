from collections import defaultdict


def dfs(node):
    if node in vis: return
    for n in lst:
        if n not in kids[node]: return
    lst.append(node)
    vis.add(node)
    for kiddo in kids[node]:
        dfs(kiddo)


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        edges = []
        kids = defaultdict(set)
        for line in fptr:
            lst = line.strip().split('-')
            kids[lst[0]].add(lst[1])
            kids[lst[1]].add(lst[0])

        maxi_lst = []
        for par in kids:
            vis = set()
            lst = []
            dfs(par)
            maxi_lst = lst if len(lst) > len(maxi_lst) else maxi_lst

        print(','.join(sorted(maxi_lst)))
