from collections import defaultdict


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        raw_data = fptr.read().strip().split('\n\n')

        locks = defaultdict(int)
        keys = defaultdict(int)
        for ele in raw_data:
            curr = ele.split('\n')
            vals = []

            for j in range(5):
                count = 0
                for i in range(1, 6):
                    if curr[i][j] == '#':
                        count += 1
                vals.append(count)
            store = tuple(vals)
            if curr[0][0] == '#':
                locks[store] += 1
            else:
                keys[store] += 1

        ans = 0
        for lock in locks:
            check = (5-lock[0], 5-lock[1], 5-lock[2], 5-lock[3], 5-lock[4])
            for key in keys:
                if key[0] <= check[0] and key[1] <= check[1] and key[2] <= check[2] and key[3] <= check[3] \
                        and key[4] <= check[4]:
                    ans += locks[lock] * keys[key]
        print(ans)





