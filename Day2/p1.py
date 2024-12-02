if __name__ == '__main__':
    fptr = open('input.txt', 'r')
    lsts = []
    for line in fptr:
        lst = list(map(int, line.rstrip().split()))
        lsts.append(lst)


    def check(lst):
        for i in range(len(lst)-1):
            if not (1 <= lst[i]-lst[i+1] <= 3): return False
        return True

    ans = 0
    for lst in lsts:
        if check(lst): ans += 1
        elif check(lst[::-1]): ans += 1
    print(ans)
    fptr.close()
