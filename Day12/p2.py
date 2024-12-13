DIR = [0, 1, 0, -1, 0]


def get_sides():
    sides = 0
    corners = set()
    diff = [(.5, .5), (.5, -.5), (-.5, .5), (-.5, -.5)]
    for x, y in region:
        for dx, dy in diff:
            corners.add((x + dx, y + dy))

    for x, y in corners:
        pattern = ""
        for dx, dy in diff:
            pattern += "X" if (x + dx, y + dy) in region else "O"
        if pattern in ("OXXO", "XOOX"):
            # When an edge coord is two the region meets itself all catty-corner

            # XOOX
            # XOOX
            # XXXX
            # XXXX

            # OXXO
            # OXXO
            # XXXX
            # XXXX

            sides += 2

        elif pattern.count("X") == 3 or pattern.count("O") == 3:
            # For when an edge coord is an interior or exterior corner.

            # XXXX
            # XOOO
            # XOOO
            # XOOO

            # OOOO
            # OXXX
            # OXXX
            # OXXX

            sides += 1

    return sides


def dfs(i, j):
    if 0 <= i < ROW and 0 <= j < COL and (i, j) not in vis:
        vis.add((i, j))
        region.add((i, j))
        plant = fence[i][j]
        area[0] += 1
        for k in range(4):
            r, c = i + DIR[k], j + DIR[k+1]
            if 0 <= r < ROW and 0 <= c < COL:
                if fence[r][c] == plant: dfs(r, c)


if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        fence = []
        for line in fptr:
            fence.append(list(line.strip()))

    vis = set()
    ROW, COL = len(fence), len(fence[0])
    ans = 0
    for i in range(ROW):
        for j in range(COL):
            if (i, j) not in vis:
                area = [0]
                region = set()
                dfs(i, j)
                sides = get_sides()
                ans += area[0] * sides
    print(ans)
