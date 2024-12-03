import re


def mul(a, b): return a * b


if __name__ == '__main__':
    fptr = open('input.txt', 'r')
    strs = fptr.read()
    lst = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", strs)
    i = ans = 0
    while i < len(lst):
        if lst[i] == "don't()":
            while lst[i] != "do()": i += 1
        if lst[i] != "do()": ans += eval(lst[i])
        i += 1
    print(ans)
    fptr.close()
