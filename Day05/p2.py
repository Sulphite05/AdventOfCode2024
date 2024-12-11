from collections import defaultdict


def verify(lst):
    n = len(lst)
    ins = False
    for i in range(1, n):
        for j in range(i, n):
            if lst[i - 1] in rules[lst[j]]:
                lst[j], lst[i-1] = lst[i-1], lst[j]
                ins = True
    return lst[n//2] if ins else 0


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        rules = defaultdict(set)
        check = []
        for line in fptr:
            if line != '\n':
                bef, aft = list(map(int, line.rstrip().split('|')))
                rules[bef].add(aft)
            else:
                break
        for line in fptr:
            check.append(list(map(int, line.rstrip().split(','))))
    ans = sum([verify(lst) for lst in check])
    print(ans)
