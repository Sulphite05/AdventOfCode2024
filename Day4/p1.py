def search(puzzle):
    ans = 0
    match = ['X', 'M', 'A', 'S']
    for row in puzzle:
        for i in range(len(row)-3):
            store = row[i:i+4]
            if store == match or store[::-1] == match:
                ans += 1
    return ans


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        puzz = []
        for line in fptr:
            puzz.append(list(line.strip()))

    col_puzz = [[puzz[j][i] for j in range(len(puzz[0]))] for i in range(len(puzz))]
    l_r_diag = [[puzz[len(puzz) - j - 1 + k][k] for k in range(j + 1)] for j in range(len(puzz))]
    l_r_diag += [[puzz[k][len(puzz) - j - 1 + k] for k in range(j + 1)] for j in range(len(puzz))][-2::-1]
    r_l_diag = [[puzz[len(puzz) - j - 1 + k][len(puzz)-k-1] for k in range(j + 1)] for j in range(len(puzz))]
    r_l_diag += [[puzz[j-k][k] for k in range(j + 1)] for j in range(len(puzz))][-2::-1]
    ans = search(puzz) + search(col_puzz) + search(l_r_diag) + search(r_l_diag)
    print(ans)
