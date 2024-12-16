
def make_move(lst, move):
    dx, dy = DIR[move]
    for x, y in lst:
        map[x+dx][y+dy] = map[x][y]
        map[x][y] = '.'


def move_lr():
    dx, dy = DIR[m]
    new_x, new_y = x+dx, y+dy
    
    if map[new_x][new_y] == '#': return False
    
    while map[new_x][new_y] != '.':
        new_x, new_y = new_x + dx, new_y + dy
        if map[new_x][new_y] == '#': return False
    
    while True:
        map[new_x][new_y] = map[new_x-dx][new_y-dy]
        if map[new_x][new_y] == '@':
            map[new_x - dx][new_y - dy] = '.'
            break
        new_x, new_y = new_x - dx, new_y - dy
    return True


def move_ud(level):
    dx, dy = DIR[m]
    can_move = True
    
    for x, y in level:
        new_x, new_y = x + dx, y + dy
        if map[new_x][new_y] == '#': return False
        if map[new_x][new_y] in '[]': can_move = False
    
    if can_move:
        make_move(level, m)
        return True
    
    new_level = []
    vis = set()
    for x, y in level:
        if map[x + dx][y + dy] == ".":
            continue
        elif map[x + dx][y + dy] == "]":
            if (x + dx, y + dy - 1) not in vis:
                vis.add((x + dx, y + dy - 1))
                new_level.append((x + dx, y + dy - 1))
            if (x + dx, y + dy) not in vis:
                vis.add((x + dx, y + dy))
                new_level.append((x + dx, y + dy))
        elif map[x + dx][y + dy] == "[":
            if (x + dx, y + dy) not in vis:
                vis.add((x + dx, y + dy))
                new_level.append((x + dx, y + dy))
            if (x + dx, y + dy + 1) not in vis:
                vis.add((x + dx, y + dy + 1))
                new_level.append((x + dx, y + dy + 1))
    if move_ud(new_level):
        make_move(level, m)
        return True
    return False
    

if __name__ == '__main__':
    with open('input.txt', 'r') as fptr:
        map = []
        pos = (0, 0)
        mov = ''
        DIR = {
            '^': (-1, 0),
            'v': (1, 0),
            '>': (0, 1),
            '<': (0, -1),
        }

        for i, line in enumerate(fptr):
            if line != '\n':
                l = []
                for j, char in enumerate(line):
                    match char:
                        case '.':
                            l.extend('..')
                        case '#':
                            l.extend('##')
                        case 'O':
                            l.extend('[]')
                        case '@':
                            x, y = j, len(l)
                            l.extend('@.')

                map.append(l)
            else:
                break

        for line in fptr:
            mov += line.strip()

        for m in mov:
            dx, dy = DIR[m]
            get = move_lr() if m in '<>' else move_ud([(x, y)])
            if get: 
                x, y = x + dx, y + dy

        ans = 0
        for i, line in enumerate(map):
            for j, char in enumerate(line):
                if char == '[': ans += i*100 + j

        print(ans)
        