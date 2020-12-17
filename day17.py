#day17.py

def neigbors1(point):
    return [(x,y,z) for x in range(point[0]-1,point[0]+2) for y in range(point[1]-1, point[1]+2) for z in range(point[2]-1, point[2]+2) if (x,y,z) != point]

def step1(space):
    nextspace = set()
    minlist = [min(t)-1 for t in zip(*space)]
    maxlist = [max(t)+2 for t in zip(*space)]
    minmax = list(zip(minlist, maxlist))

    for x in range(*minmax[0]):
        for y in range(*minmax[1]):
            for z in range(*minmax[2]):
                p = (x,y,z)
                c = len([n for n in neigbors1(p) if n in space])
                if p in space: #active
                    if c == 2 or c == 3:
                        nextspace.add(p)
                else:
                    if c == 3:
                        nextspace.add(p)
    return nextspace

def neigbors2(point):
    return [(x,y,z,w) for x in range(point[0]-1,point[0]+2) for y in range(point[1]-1, point[1]+2) for z in range(point[2]-1, point[2]+2) for w in range(point[3]-1, point[3]+2) if (x,y,z,w) != point]

def step2(space):
    nextspace = set()
    minlist = [min(t)-1 for t in zip(*space)]
    maxlist = [max(t)+2 for t in zip(*space)]
    minmax = list(zip(minlist, maxlist))

    for x in range(*minmax[0]):
        for y in range(*minmax[1]):
            for z in range(*minmax[2]):
                for w in range(*minmax[3]):
                    p = (x,y,z,w)
                    c = len([n for n in neigbors2(p) if n in space])
                    if p in space: #active
                        if c == 2 or c == 3:
                            nextspace.add(p)
                    else:
                        if c == 3:
                            nextspace.add(p)
    return nextspace

def part1():
    space = set()
    with open('input17.txt', 'r') as f:
        y = 0
        for line in f:
            for x,v in enumerate(line.strip()):
                if v == '#':
                    space.add((x,y,0))
            y += 1
    for i in range(6):
        space = step1(space)
    return len(space)

def part2():
    space = set()
    with open('input17.txt', 'r') as f:
        y = 0
        for line in f:
            for x,v in enumerate(line.strip()):
                if v == '#':
                    space.add((x,y,0,0))
            y += 1
    for i in range(6):
        space = step2(space)
    return len(space)

print(part1())
print(part2())
