from collections import Counter

if __name__ == '__main__':
    fptr = open('input.txt', 'r')
    lst1 = []
    lst2 = []
    for line in fptr:
        val1, val2 = list(map(int, line.rstrip().split()))
        lst1.append(val1)
        lst2.append(val2)

    c2 = Counter(lst2)
    ans = sum([a*c2.get(a, 0) for a in lst1])

    print(ans)
    fptr.close()
