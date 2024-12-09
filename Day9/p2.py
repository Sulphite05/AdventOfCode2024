if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        puzz = list(map(int, list(fptr.readline().strip())))

    space = []
    block = []
    for i in range(1, len(puzz), 2):
        space.append(puzz[i])
    space.append(0)
    for i in range(0, len(puzz), 2):
        block.append([i // 2] * puzz[i])

    block2 = []
    for lst in block:
        block2.append(lst[:])

    for i in range(len(block) - 1, -1, -1):
        bl = len(block[i])
        for j, sp in enumerate(space):
            if j == i: break
            if sp >= bl:
                space[i - 1] += bl
                space[j] -= bl
                block2[j] += block[i]
                block2[i] = block2[i][bl:]
                break
    ind = ans = 0
    for b, s in zip(block2, space):
        for num in b:
            ans += num * ind
            ind += 1
        ind += s

    print(ans)
