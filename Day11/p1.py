
def split_stones():
    new = []
    for stone in stones:
        if stone == '0':
            new.append('1')
        elif not len(stone)&1:
            num1, num2 = stone[:len(stone)//2], str(int(stone[len(stone)//2:]))
            new.extend([num1, num2])
        else:
            num = int(stone)*2024
            new.append(str(num))
    return new


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        stones = list(fptr.readline().strip().split())

    for _ in range(25):
        stones = split_stones()
    print(len(stones))

