if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        puzz = list(map(int, list(fptr.readline().strip())))

    new = []
    i = 0
    j = len(puzz) - 1
    while i <= j:
        new += [i // 2] * puzz[i]
        i += 1
        while i <= j and puzz[i]:
            if puzz[j] <= puzz[i]:
                new += [j // 2] * puzz[j]
                puzz[i] -= puzz[j]
                puzz[j] = 0
                j -= 2

            else:
                new += [j // 2] * puzz[i]
                puzz[j] -= puzz[i]
                puzz[i] = 0
        i += 1

    ans = sum([num * i for i, num in enumerate(new)])
    print(ans)
