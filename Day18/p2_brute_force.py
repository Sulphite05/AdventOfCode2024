from heapq import heappop, heappush

if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        st = (0, 0)
        en = (70, 70)
        bytes = []
        for i, line in enumerate(fptr):
            bytes.append(tuple(map(int, list(eval(line)))))

        DIR = {'E': (0, 1),
               'W': (0, -1),
               'N': (-1, 0),
               'S': (1, 0)}

        i, j = 0, len(bytes) - 1
        while i < j:
            mid = (i + j) >> 1
            curr_bytes = set(bytes[:mid+1])
            heap = [[0, st]]
            vis = set()
            while heap:
                cost, loc = heappop(heap)
                if loc in vis:
                    continue
                else:
                    vis.add(loc)
                if loc == en:
                    i = mid + 1
                    break
                for direct in DIR:
                    x, y = loc[0] + DIR[direct][0], loc[1] + DIR[direct][1]
                    if 0 <= x <= en[0] and 0 <= y <= en[1] and (x, y) not in curr_bytes:
                        c = cost + 1
                        heappush(heap, [c, (x, y)])
            else:
                j = mid

        print(bytes[mid+1])
