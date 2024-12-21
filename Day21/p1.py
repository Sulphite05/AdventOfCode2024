def create_rob(pad, seq):
    curr = 'A'
    rob1_seq = []
    for digit in seq:
        if digit != curr:
            a, b = pad[curr]
            c, d = pad[digit]
            dx = c - a
            dy = d - b
            h = '<' * -dy + '>' * dy
            v = '^' * -dx + 'v' * dx
            if dy > 0 and (c, b) not in pad:
                rob1_seq.extend(v + h)
            elif (a, d) not in pad:
                rob1_seq.extend(h + v)
            else:
                rob1_seq.extend(v + h)
        rob1_seq.append('A')
        curr = digit
    return rob1_seq


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        sequences = []
        for line in fptr:
            sequences.append(line.strip())

        one_dir_keypad = {'7': (0, 0), '8': (0, 1), '9': (0, 2),
                          '4': (1, 0), '5': (1, 1), '6': (1, 2),
                          '1': (2, 0), '2': (2, 1), '3': (2, 2),
                          (3, 0): ' ', '0': (3, 1), 'A': (3, 2)}

        bi_dir_keypad = {(0, 0): ' ', '^': (0, 1), 'A': (0, 2),
                         '<': (1, 0), 'v': (1, 1), '>': (1, 2)}

        ans = 0
        for seq in sequences:
            rob1 = create_rob(one_dir_keypad, seq)
            rob2 = create_rob(bi_dir_keypad, rob1)
            rob3 = create_rob(bi_dir_keypad, rob2)
            ans += len(rob3)*int(seq[:-1])
        print(ans)
