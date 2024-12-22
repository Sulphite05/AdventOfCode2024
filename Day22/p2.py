from collections import defaultdict, deque


def mix_prune(num, new):
    return (num ^ new) % MOD


MOD = 16777216  # need last 24 bits only
if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        sequences = []
        for line in fptr:
            sequences.append(int(line.strip()))

    l = len(sequences)
    c = defaultdict(lambda: [0] * l)  # seq: value of seq reaped in every secret

    for ind, num in enumerate(sequences):
        lst = deque()
        prev = num % 10
        for i in range(2000):
            num = mix_prune(num, num << 6)
            num = mix_prune(num, num >> 5)
            num = mix_prune(num, num << 11)
            curr = num % 10
            change = curr - prev
            lst.append(change)
            prev = curr
            if i > 2:
                st = tuple(lst)
                if not c[st][ind]: c[st][ind] = max(c[st][ind], curr)
                lst.popleft()

    maxi = 0
    for key in c:
        maxi = max(maxi, sum(c[key]))
    print(maxi)
