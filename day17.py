#day17.py
import unittest
from itertools import product

def neighbors(point):
    return [v for v in product(*[range(p-1, p+2) for p in point]) if v != point]

def searchfield(space):
    return list(product(*[range(min(t)-1, max(t)+2) for t in zip(*space)]))

def step(space):
    nextspace = set()
    for p in searchfield(space):
        c = len([n for n in neighbors(p) if n in space])
        if c == 3 or (c == 2 and p in space):
            nextspace.add(p)
    return nextspace

def conway(dimension, filename='input17.txt', cycles=6):
    space = set()
    with open(filename, 'r') as f:
        y = 0
        for line in f:
            for x,v in enumerate(line.strip()):
                if v == '#':
                    space.add(tuple([x,y] +[0]*(dimension-2)))
            y += 1
    for i in range(cycles):
        space = step(space)
    return len(space)

print(conway(3))
print(conway(4))
