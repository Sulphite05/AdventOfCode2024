def fitness(a, j):
    if j == -1:
        return a
    for _ in range(8):
        a += 1
        b = (a % 8) ^ 1
        c = a >> b
        val = ((b ^ 5) ^ c) % 8
        if val == program[j]:
            store = fitness(a * 8, j - 1)
            if store:
                print(a)
                return a
    return None


registers = dict()
registers.update({0: 0, 1: 1, 2: 2, 3: 3})
program = [2, 4, 1, 1, 7, 5, 1, 5, 4, 1, 5, 5, 0, 3, 3, 0]
l = len(program)
# This program is exclusively written to solve the puzzle 2,4,1,1,7,5,1,5,4,1,5,5,0,3,3,0
get = fitness(0, l - 1)
print(get)
