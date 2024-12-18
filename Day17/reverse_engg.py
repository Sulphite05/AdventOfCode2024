def fitness(a, j):
    if j == 0: return a
    for _ in range(8):
        a += 1
        b = (a % 8) ^ 1
        c = a >> b
        val = ((b ^ 5) ^ c) % 8
        if val == program[j]:
            store = fitness(a << 3, j - 1)
            if store: return store
    return None


program = [2, 4, 1, 1, 7, 5, 1, 5, 4, 1, 5, 5, 0, 3, 3, 0]
l = len(program)
# This program is exclusively written to solve the puzzle 2,4,1,1,7,5,1,5,4,1,5,5,0,3,3,0
get = fitness(0, l - 1)
print(get)
