from collections import Counter


def routes1(seq):
    rob1_seq = []
    curr = 'A'
    for digit in seq:
        rob1_seq.append(create_rob(curr, digit))
        curr = digit
    return ''.join(rob1_seq)


def routes2(seq):
    rob1_seq = []
    curr = 'A'
    for digit in seq:
        rob1_seq.append(create_rob(curr, digit))
        curr = digit
    return Counter(rob1_seq)


def create_rob(curr, digit):
    a, b = pad[curr]
    c, d = pad[digit]
    dx = c - a
    dy = d - b
    h = '<' * -dy + '>' * dy
    v = '^' * -dx + 'v' * dx
    if dy > 0 and (c, b) not in pad:
        return v + h + 'A'
    elif (a, d) not in pad:
        return h + v + 'A'
    else:
        return v + h + 'A'


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

        pad = one_dir_keypad
        robot_routes = [Counter([routes1(seq)]) for seq in sequences]
        pad = bi_dir_keypad
        ans = 0
        for _ in range(25):
            new_routes = []
            for route_counter in robot_routes:
                new_route = Counter()
                for sub_route, qty in route_counter.items():
                    new_counts = routes2(sub_route)
                    for k in new_counts:
                        new_counts[k] *= qty
                    new_route.update(new_counts)
                new_routes.append(new_route)
            robot_routes = new_routes

        totals = []
        for lines, seq in zip(robot_routes, sequences):
            summ = 0
            for k, val in lines.items():
                summ += val * len(k)
            totals.append(summ * int(seq[:-1]))
        print(sum(totals))
