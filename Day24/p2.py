def swap(eq1, eq2):
    eq_to_var[eq1], eq_to_var[eq2] = eq_to_var[eq2], eq_to_var[eq1]
    ans.extend([eq_to_var[eq1], eq_to_var[eq2]])


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        for line in fptr:
            if line == '\n': break

        eq_to_var = dict()
        tot = 45
        for line in fptr:
            op1, op, op2, _, out = line.strip().split()
            eq_to_var[(op1, op2, op)] = out

        check = lambda k, op1, op2, op: k == (op1, op2, op) or k == (op2, op1, op)
        ans = []
        c_old = ''
        for i in range(tot):
            xor_eq = and_eq = c_and_eq = c_eq = sum_eq = ''
            x, y, z = f'x{i:02}', f'y{i:02}', f'z{i:02}'

            for eq in eq_to_var:
                if check(eq, x, y, 'XOR'): xor_eq = eq
                if check(eq, x, y, 'AND'): and_eq = eq

            if c_old:
                for eq in eq_to_var:
                    if check(eq, eq_to_var[c_old], eq_to_var[xor_eq], 'AND'): c_and_eq = eq
                if not c_and_eq:
                    swap(xor_eq, and_eq)
                    for eq in eq_to_var:
                        if check(eq, eq_to_var[c_old], eq_to_var[xor_eq], 'AND'): c_and_eq = eq

                for eq in eq_to_var:
                    if check(eq, eq_to_var[c_old], eq_to_var[xor_eq], 'XOR'): sum_eq = eq
                if xor_eq and eq_to_var[xor_eq][0] == 'z': swap(xor_eq, sum_eq)
                if and_eq and eq_to_var[and_eq][0] == 'z': swap(and_eq, sum_eq)
                if c_and_eq and eq_to_var[c_and_eq][0] == 'z': swap(c_and_eq, sum_eq)

                for eq in eq_to_var:
                    if check(eq, eq_to_var[c_and_eq], eq_to_var[and_eq], 'OR'): c_eq = eq
            if c_eq and eq_to_var[c_eq][0] == 'z' and eq_to_var[c_eq] != 'z45':
                swap(c_eq, sum_eq)
            c_old = c_eq if c_old else and_eq

        print(','.join(sorted(ans)))


# 18460186568099:  100001100101000011000110111001110010110100011 x
# 34461222108877:  111110101011110100000111001101111111011001101 y
# 52921408676976: 1100000010000110111001110000111110010001110000 z_actual
# 52956035802096: 1100000010100111001001101100111110001111110000 z_wrong
