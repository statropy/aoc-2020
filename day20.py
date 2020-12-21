#day20.py
import math
import re

def getedges(tile):
    for line in tile:
        size = len(tile)
        top = int(tile[0],2)
        right, bottom, left = 0,0,0
        for i,line in enumerate(tile):
            if line[-1] == '1':
                right |= (1 << (size-i-1))
            if line[0] == '1':
                left |= (1 << i)
            if tile[-1][i] == '1':
                bottom |= (1 << i)
        return [top, right, bottom, left]

#chenage to return new list
def rev(tile):
    revtile = []
    for line in tile:
        x = list(line)
        x.reverse()
        revtile.append(''.join(x))
    return revtile

tilemap = {}
with open('input20.txt', 'r') as f:
    tileid = 0

    for line in f:
        if line[0] == 'T':
            tileid = int(line[5:-2])
            tilemap[tileid] = []
        elif len(line) > 1:
            tilemap[tileid].append(line.strip().replace('.','0').replace('#','1'))
size = len(next(iter(tilemap.values())))
mask = (1<<size)-1
width = int(math.sqrt(len(tilemap)))

edges = {}
edgecount = {}
for tileid,tile in tilemap.items():
    front = getedges(tile)
    back = getedges(rev(tile))
    edges[tileid] = [front, back]
    for edge in front+back:
        edgecount.setdefault(edge, [])
        edgecount[edge].append(tileid)

def other_edges(edges, tile):
    edgecount = {}
    for tileid,(front, back) in edges.items():
        if tileid == tile: continue
        for edge in front + back:
            edgecount.setdefault(edge, [])
            edgecount[edge].append(tileid)
    return edgecount


corners = set()
sides = set()
middles = set()

puzzlemap = {}

for tileid,(front, back) in edges.items():
    front_matches, back_matches = 0,0
    puzzlemap[tileid] = [None, None, None, None]
    for i,edge in enumerate(front):
        matches = [e for e in edgecount[edge] if e != tileid]
        if len(matches) == 1:
            puzzlemap[tileid][i] = matches[0]
            front_matches += 1
        elif len(matches) > 0:
            print('Too many', tileid, matches)
    if front_matches == 2:
        corners.add(tileid)
    if front_matches == 3:
        sides.add(tileid)
    else:
        middles.add(tileid)

def rotate(tileid, pmap, tmap):
    pmap[tileid].insert(0, pmap[tileid].pop())
    tmap[tileid] = [''.join(x) for x in zip(*tmap[tileid][::-1])]

def shrink(oldpiece):
    piece = []
    for i in range(1, len(oldpiece)-1):
        s = oldpiece[i][1:-1]
        piece.append(s)
    return piece

def findnext(puzzlemap, tilemap, puzzlegrid, imagegrid, current, bottom=True, puzrow=None, gridrow=None):
    current_line = ''
    if bottom:
        #print('finding bottom of', current)
        current_line = tilemap[current][-1]
    else:
        #print('finding right of', current)
        current_line = ''.join([line[-1] for line in tilemap[current]])

    for tile in [x for x in puzzlemap[current] if x is not None]:
        tile_text = tilemap[tile]
        found = False
        rotations = 0
        for rotations in range(8):
            tile_line = ''
            if bottom:
                tile_line = tile_text[0]
            else:
                tile_line = ''.join([line[0] for line in tile_text])

            if tile_line == current_line:
                found = True
                break
            else:
                if rotations == 3:
                    #print('flip')
                    for i,line in enumerate(tile_text):
                        line = list(line)
                        line.reverse()
                        tile_text[i] = ''.join(line)
                else:
                    tile_text = [''.join(x) for x in zip(*tile_text[::-1])]
        if found:
            for r,line in enumerate(tile_text):
                if puzrow is None:
                    puzzlegrid.append(line)
                else:
                    puzzlegrid[puzrow+r] += line
            for r,line in enumerate(shrink(tile_text)):
                if gridrow is None:
                    imagegrid.append(line)
                else:
                    imagegrid[gridrow+r] += line

            tilemap[tile] = tile_text
            puzzlemap[current][puzzlemap[current].index(tile)] = None
            puzzlemap[tile][puzzlemap[tile].index(current)] = None
            return tile

topleft = next(iter(corners))

r = 0
while (puzzlemap[topleft][0] is not None) or (puzzlemap[topleft][3] is not None):
    rotate(topleft, puzzlemap, tilemap)
    r += 1

puzzlegrid = []
imagegrid = []

for line in tilemap[topleft]:
    puzzlegrid.append(line)

for line in shrink(tilemap[topleft]):
    imagegrid.append(line)

current = topleft
topofrow = topleft

for line in tilemap[current]:
    puzzlegrid.append(line)

#first column
for i in range(1, width):
    current = findnext(puzzlemap, tilemap, puzzlegrid, imagegrid, current)

for col in range(1, width):
    #top of colum
    topofrow = findnext(puzzlemap, tilemap, puzzlegrid, imagegrid, topofrow, False, 0, 0)
    current = topofrow
    #rest of column
    for row in range(1, width):
        current = findnext(puzzlemap, tilemap, puzzlegrid, imagegrid, current, True, size*row, (size-2)*row)

midline = re.compile(r'1....11....11....111')
bottomline = re.compile(r'1..1..1..1..1..1')


for i,line in enumerate(imagegrid):
    imagegrid[i] = line.replace('0',' ')

matches = 0
finalgrid = None
middlelist = [0,5,6,11,12,17,18,19]
bottomlist = [1,4,7,10,13,16]

for rotations in range(8):
    for i,line in enumerate(imagegrid):
        if i == 0 or i == len(imagegrid)-1: continue
        
        for m in midline.findall(line):
            idx = line.index(m)
            if imagegrid[i-1][idx+18] == '1':
                bottommatch = sum([1 for x in bottomlist if imagegrid[i+1][x+idx] == '1'])
                if bottommatch == len(bottomlist):
                    matches += 1
                    if finalgrid is None:
                        finalgrid = [x for x in imagegrid]

                    fgl = list(finalgrid[i-1])
                    fgl[idx+18] = 'O'
                    finalgrid[i-1] = ''.join(fgl)
                    
                    fgl = list(finalgrid[i])
                    for z in middlelist:
                        fgl[idx+z] = 'O'
                    finalgrid[i] = ''.join(fgl)

                    fgl = list(finalgrid[i+1])
                    for z in bottomlist:
                         fgl[idx+z]= 'O'
                    finalgrid[i+1] = ''.join(fgl)
    if matches == 0:
        if rotations == 3:
            #print('flip')
            for i,line in enumerate(imagegrid):
                line = list(line)
                line.reverse()
                imagegrid[i] = ''.join(line)
        else:
            imagegrid = [''.join(x) for x in zip(*imagegrid[::-1])]
    else:
        break

total = 0
for line in imagegrid:
    total += line.count('1')

final = 0
for line in finalgrid:
    final += line.count('1')

#part 1 answer
prod = 1
for c in corners:
    prod *= c
print(prod)
print(final)
