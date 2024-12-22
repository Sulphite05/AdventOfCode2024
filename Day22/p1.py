def mix_prune(num, new):
    return (num ^ new) % MOD


MOD = 16777216  # need last 24 bits only
if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        sequences = []
        for line in fptr:
            sequences.append(int(line.strip()))
    ans = 0
    for num in sequences:
        for _ in range(2000):
            num = mix_prune(num, num << 6)
            num = mix_prune(num, num >> 5)
            num = mix_prune(num, num << 11)
        ans += num
    print(ans)
