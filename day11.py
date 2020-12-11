#day11.py

def make_map(width, depth):
    m = []
    for i in range(depth):
        m += [['.']*width]
    return m

def search1(m, n, r, c, w, d):
    seat = m[r][c]
    if seat == '.': 
        n[r][c] = '.'
        return False

    checks = [(row,col) for row in range(r-1, r+2) for col in range(c-1, c+2) if row >= 0 and row < d and col >= 0 and col < w and (row,col) != (r,c)]

    if seat == 'L':
        for row, col in checks:
            if m[row][col] == '#':
                n[r][c] = 'L'
                return False
        n[r][c] = '#'
        return True

    count = 0
    for row, col in checks:
        if m[row][col] == '#':
            count += 1
    if count >= 4:
        n[r][c] = 'L'
        return True
    n[r][c] = '#'
    return False

def valid(y, x, w, d):
    return y >= 0 and y < d and x >= 0 and x < w

def search2(m, n, r, c, w, d):
    seat = m[r][c]
    if seat == '.': 
        n[r][c] = '.'
        return False

    vectors = [(row,col) for row in range(-1, 2) for col in range(-1, 2) if (row,col) != (0,0)]

    if seat == 'L':
        for y, x in vectors:
            row, col = r+y, c+x
            while valid(row, col, w, d):
                if m[row][col] == '#':
                    n[r][c] = 'L'
                    return False
                elif  m[row][col] == 'L':
                    break
                row, col = row+y, col+x
        n[r][c] = '#'
        return True

    count = 0
    for y, x in vectors:
        row, col = r+y, c+x
        while valid(row, col, w, d):
            if m[row][col] == '#':
                count += 1
                if count >= 5:
                    n[r][c] = 'L'
                    return True
                break
            elif  m[row][col] == 'L':
                break
            row, col = row+y, col+x
    n[r][c] = '#'
    return False

def find_seats(search, limit=1000, filename='input11.txt'):
    before = [[c for c in line.strip()] for line in open(filename, 'r')]
    width = len(before[0])
    depth = len(before)
    after = make_map(width, depth)

    runs = 1
    while runs <= limit:
        changes = len([1 for r in range(depth) for c in range(width) if search(before, after, r, c, width, depth)])

        if changes == 0:
            print("%d (%d runs)" % (len([1 for r in range(depth) for c in range(width) if after[r][c] == '#']), runs))
            break
        else:
            before, after = after, before
        runs += 1

if __name__ == '__main__':
    find_seats(search1)
    find_seats(search2)
