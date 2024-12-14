import re
from collections import Counter

if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        pos = []
        vel = []
        for line in fptr:
            a, b = re.findall('[0-9]+', line)[:2]
            get = re.findall('[0-9]+|-[0-9]+', line)
            x = get[-2]
            y = get[-1]
            pos.append([int(a), int(b)])
            vel.append((int(x), int(y)))

    w, h, n = 101, 103, 100

    for i in range(len(pos)):
        a, b = pos[i][0], pos[i][1]
        x, y = vel[i][0], vel[i][1]
        x = (((a + x * n) % w) + w) % w
        y = (((b + y * n) % h) + h) % h
        pos[i][0], pos[i][1] = x, y
        pos[i] = tuple(pos[i])

    n_w, n_h = w // 2, h // 2
    c = Counter(pos)
    one = two = three = four = 0
    for a, b in pos:
        if 0 <= a < n_w and 0 <= b < n_h and (a, b) in c:
            one += c[(a, b)]
            del c[(a, b)]

        elif n_w < a < w and 0 <= b < n_h and (a, b) in c:
            two += c[(a, b)]
            del c[(a, b)]

        elif 0 <= a < n_w and n_h < b < h and (a, b) in c:
            three += c[(a, b)]
            del c[(a, b)]

        elif n_w < a < w and n_h < b < h and (a, b) in c:
            four += c[(a, b)]
            del c[(a, b)]

    ans = one * two * three * four
    print(ans)

