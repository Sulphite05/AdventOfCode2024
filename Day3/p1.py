import re


def mul(a, b): return a * b


if __name__ == '__main__':
    fptr = open('input.txt', 'r')
    strs = fptr.read()
    lst = re.findall('mul\([0-9]+,[0-9]+\)', strs)
    ans = sum([eval(func) for func in lst])
    print(ans)
    fptr.close()
