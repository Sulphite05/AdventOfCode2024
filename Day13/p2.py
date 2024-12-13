import re

if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        eq = [[], [], [], [], [], []]  # a,b,c,d,e,f
        for line in fptr:
            a, d = re.findall('[0-9]+', line)
            eq[0].append(int(a))
            eq[3].append(int(d))
            b, e = re.findall('[0-9]+', fptr.readline())
            eq[1].append(int(b))
            eq[4].append(int(e))
            c, f = re.findall('[0-9]+', fptr.readline())
            eq[2].append(int(c) + 10000000000000)
            eq[5].append(int(f) + 10000000000000)
            fptr.readline()

        ans = 0
        for i in range(len(eq[0])):
            a, b, c, d, e, f = [eq[j][i] for j in range(len(eq))]
            y = (d * c - f * a) / (-(-b * d + e * a))
            if int(y) == y:
                ans += int(y)
            else:
                continue
            x = (c - b * y) / a
            if int(x) == x:
                ans += int(x) * 3

        print(ans)
