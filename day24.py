#day24.py
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

steps = {'e':Point(2,0), 'w':Point(-2,0), 'ne':Point(1,1), 'se':Point(1,-1), 'nw':Point(-1,1), 'sw':Point(-1,-1)}

def add(p1, p2):
    return Point(p1.x+p2.x, p1.y+p2.y)

def part1(routes):
    hexmap = set()
    for route in routes:
        pos = Point(0,0)
        partial = None
        direction = None
        for c in route:
            if c in 'sn':
                partial = c
                continue
            if partial:
                direction = partial+c
            else:
                direction = c
            if direction == 'e':
                step = Point
            pos = add(pos, steps[direction])
            partial = None
        if pos in hexmap:
            hexmap.remove(pos)
        else:
            hexmap.add(pos)
    print(len(hexmap))
    return hexmap

def neighbors(pos):
    return [add(pos, p) for p in steps.values()]

def black_filter(hexmap, n):
    return [p for p in n if p in hexmap]

def black_neighbors(hexmap, pos):
    n = neighbors(pos)
    return black_filter(hexmap, n)

def step2(hexmap):
    nextmap = set()
    tocheck = set()
    for pos in hexmap:
        n = neighbors(pos)
        bn = len(black_filter(hexmap, n))
        if bn == 1 or bn == 2:
            nextmap.add(pos)
        tocheck |= set(n)

    tocheck -= hexmap
    for pos in tocheck:
        if len(black_neighbors(hexmap, pos)) == 2:
            nextmap.add(pos)
    return nextmap


def part2(hexmap, rounds=100):
    for i in range(rounds):
        hexmap = step2(hexmap)
    print(len(hexmap))

routes = [line.strip() for line in open('input24.txt', 'r')]
blacktiles = part1(routes)
part2(blacktiles, 100)
