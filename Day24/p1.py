def dfs(out):
    if out in vis: return values[out]
    vis.add(out)
    op1, op, op2 = dependents[out]
    op1 = dfs(op1)
    op2 = dfs(op2)
    match op:
        case 'XOR':
            ans = op1 ^ op2
        case 'AND':
            ans = op1 & op2
        case 'OR':
            ans = op1 | op2
    values[out] = ans
    return ans


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        vis = set()
        values = dict()
        for line in fptr:
            if line == '\n': break
            inp, val = line.strip().split(': ')
            values[inp] = int(val)
            vis.add(inp)

        outs = []
        dependents = dict()

        for line in fptr:
            op1, op, op2, _, out = line.strip().split()
            dependents[out] = [op1, op, op2]
            if out[0] == 'z': outs.append(out)
        outs.sort(reverse=True)
        final = ''

        for out in outs:
            final += str(dfs(out))

        print(int(final, 2))

