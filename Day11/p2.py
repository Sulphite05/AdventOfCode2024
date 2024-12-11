from collections import Counter, defaultdict


def split_stones():
    new = defaultdict(int)
    for stone in stones:
        if stone == '0': num = '1'
        elif not len(stone)&1:
            num1, num = stone[:len(stone)//2], str(int(stone[len(stone)//2:]))
            new[num1] += stones[stone]
        else: num = str(int(stone)*2024)
        new[num] += stones[stone]
    return new


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        stones = Counter(list(fptr.readline().strip().split()))

    for _ in range(75):
        stones = split_stones()
    print(sum(stones[key] for key in stones))

