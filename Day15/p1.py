def check(a, b):
    return 0 <= a < H and 0 <= b < W


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        stones = set()
        walls = set()
        pos = (0, 0)
        mov = ''
        DIR = {
            '^': (-1, 0),
            'v': (1, 0),
            '>': (0, 1),
            '<': (0, -1),
        }

        for i, line in enumerate(fptr):
            if line != '\n':
                W = len(line) - 1
                for j, char in enumerate(line):
                    match char:
                        case '#':
                            walls.add((i, j))
                        case 'O':
                            stones.add((i, j))
                        case '@':
                            pos = (i, j)
            else:
                H = i
                break
        for line in fptr:
            mov += line.strip()

        for m in mov:
            a, b = pos[0] + DIR[m][0], pos[1] + DIR[m][1]
            if check(a, b) and (a, b) not in walls:
                c, d = a, b
                if (a, b) not in stones:
                    pos = (c, d)
                    continue
                while (c, d) in stones:
                    c, d = c + DIR[m][0], d + DIR[m][1]
                    if (c, d) in walls:
                        break
                else:
                    if check(c, d):
                        if (c, d) not in walls:
                            stones.add((c, d))
                            stones.remove((a, b))
                            pos = (a, b)

        ans = 0
        for r, c in stones:
            ans += r * 100 + c
        print(ans)
