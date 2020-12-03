#day3.py
import math

def traverse(m,right=3,down=1,width=31):
    x, y, count = 0,0,0
    while y < len(m):
        if m[y][x] == '#':
            count += 1
        x = (x+right) % width
        y = y + down
    return count

if __name__ == '__main__':
    treemap = []
    with open('input3.txt', 'r') as f:
        treemap = [line.strip() for line in f]
    width = len(treemap[0])

    print(traverse(treemap, 3, 1, width))

    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    print(math.prod([traverse(treemap, r, d, width) for (r,d) in slopes]))
