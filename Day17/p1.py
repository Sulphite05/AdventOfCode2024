import re

if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        registers = dict()
        registers['4'] = int(re.findall('[0-9]+', fptr.readline())[0])
        registers['5'] = int(re.findall('[0-9]+', fptr.readline())[0])
        registers['6'] = int(re.findall('[0-9]+', fptr.readline())[0])
        registers.update({'0': 0, '1': 1, '2': 2, '3': 3})
        fptr.readline()
        program = re.findall('[0-9]+', fptr.readline())

        i = 0
        end = len(program)-1
        out = []

        while i < end:
            op = program[i + 1]
            match program[i]:
                case '0':
                    registers['4'] //= 2 ** registers[op]
                case '1':
                    registers['5'] ^= int(op)
                case '2':
                    registers['5'] = registers[op] % 8
                case '3':
                    if registers['4']:
                        i = int(op)
                        continue
                case '4':
                    registers['5'] ^= registers['6']
                case '5':
                    print(registers[op] % 8, registers[op])
                    out.append(registers[op] % 8)
                case '6':
                    registers['5'] = registers['4'] // 2 ** registers[op]
                case '7':
                    registers['6'] = registers['4'] // 2 ** registers[op]
            # print(registers['4'], registers['5'], registers['6'])
            i += 2

    print(','.join(map(str, out)))
