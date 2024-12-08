from collections import defaultdict

if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        map = defaultdict(list)
        for i, line in enumerate(fptr):
            for j, char in enumerate(line):
                if char!='.' and char!='\n': map[char].append((i, j))

    row, col = i, j
    antinodes = set()
    for node in map:
        lst = map[node]
        l = len(lst)
        for i in range(l):
            a, b = lst[i]
            for j in range(i+1, l):
                c, d = lst[j]
                diff_r, diff_c = a-c, b-d
                an1_r, an1_c = a + diff_r, b + diff_c
                an2_r, an2_c = c - diff_r, d - diff_c
                if 0 <= an1_r <= row and 0 <= an1_c <= col: antinodes.add((an1_r, an1_c))
                if 0 <= an2_r <= row and 0 <= an2_c <= col: antinodes.add((an2_r, an2_c))

    print(len(antinodes))
