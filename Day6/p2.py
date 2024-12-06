from p1 import solve

if __name__ == '__main__':
    vis, area, r, c = solve()
    m, n = len(area), len(area[0])
    dir = [-1, 0, 1, 0]  # u r d l
    row, col = r, c
    ans = 0

    for i, j in vis:
        r, c = row, col
        vis_area_dir = set()
        a, b = 0, 1
        while True:
            if (r, c, a, b) in vis_area_dir:
                ans += 1
                break
            vis_area_dir.add((r, c, a, b))
            r += dir[a]
            c += dir[b]

            if not (0 <= r < m and 0 <= c < n): break
            if area[r][c] == '#' or (r == i and c == j):
                r -= dir[a]
                c -= dir[b]
                a, b = (a + 1) % 4, (b + 1) % 4

    print(ans)
