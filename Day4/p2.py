def search(puzzle):
    ans = 0
    match = ['M', 'A', 'S']
    # M.S
    # .A.
    # M.S
    for i in range(len(puzzle)-2):
        for j in range(len(puzzle)-2):
            store1 = [puzzle[i + 0][j + 0], puzzle[i + 1][j + 1], puzzle[i + 2][j + 2]]
            store2 = [puzzle[i + 0][j + 2], puzzle[i + 1][j + 1], puzzle[i + 2][j + 0]]
            if (store1 == match or store1[::-1] == match) and (store2 == match or store2[::-1] == match):
                ans += 1
    return ans


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        puzz = []
        for line in fptr:
            puzz.append(list(line.strip()))

    print(search(puzz))
