if __name__ == '__main__':
    fptr = open('input.txt', 'r')
    lsts = []
    for line in fptr:
        lst = list(map(int, line.rstrip().split()))
        lsts.append(lst)

    def get_ans(lst):
        for i in range(len(lst)-1):
            if not (1 <= lst[i]-lst[i+1] <= 3): return False
        return True

    def check(lst):
        val = get_ans(lst)
        for i in range(len(lst)):
            if not val: val = get_ans(lst[:i]+lst[i+1:])
            else: return True
        return val

    ans = 0
    for lst in lsts:
        if check(lst): ans += 1
        elif check(lst[::-1]): ans += 1
    print(ans)
    fptr.close()
