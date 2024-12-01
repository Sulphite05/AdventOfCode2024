from collections import Counter

if __name__ == '__main__':
    fptr = open('input.txt', 'r')
    lst1 = []
    lst2 = []
    for line in fptr:
        val1, val2 = list(map(int, line.rstrip().split()))
        lst1.append(val1)
        lst2.append(val2)

    lst1.sort()
    lst2.sort()

    ans = sum([abs(a-b) for a, b in zip(lst1, lst2)])
    print(ans)
    fptr.close()
