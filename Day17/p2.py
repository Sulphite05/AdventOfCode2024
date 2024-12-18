import re


def fitness(a, ind):
    if ind == 0: return a
    for _ in range(8):
        a += 1
        registers['4'] = a
        i = 0
        end = len(program) - 1
        cont = False
        while i < end:
            op = program[i + 1]
            match program[i]:
                case '0':
                    registers['4'] <<= registers[op]
                case '1':
                    registers['5'] ^= int(op)
                case '2':
                    registers['5'] = registers[op] % 8
                case '3':
                    if cont:
                        get = fitness(registers['4'], ind - 1)
                        if get: return get
                    break
                case '4':
                    registers['5'] ^= registers['6']
                case '5':
                    val = registers[op] % 8
                    if val == int(program[ind]): cont = True
                    else: break
                case '6':
                    registers['5'] = registers['4'] >> registers[op]
                case '7':
                    registers['6'] = registers['4'] >> registers[op]
            i += 2
    return None


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        registers = dict()
        fptr.readline()
        fptr.readline()
        fptr.readline()
        registers['4'] = 0
        registers['5'] = 0
        registers['6'] = 0
        registers.update({'0': 0, '1': 1, '2': 2, '3': 3})
        fptr.readline()
        program = re.findall('[0-9]+', fptr.readline())
        l = len(program)
        print(fitness(0, l-1))
