#day12.py

def update_pos(pos, h, v):
    if h == 'N':
        return pos[0], pos[1]-v
    elif h == 'S':
        return pos[0], pos[1]+v
    elif h == 'E':
        return pos[0]+v, pos[1]
    elif h == 'W':
        return pos[0]-v, pos[1]

def part1(filename='input12.txt'):
    directions = [(line[0],int(line[1:])) for line in open(filename, 'r').read().split()]

    headings = {0:'N', 90:'E', 180:'S', 270:'W'}
    orientation = 90
    pos = (0,0)

    for h, v in directions:
        if h == 'L':
            orientation -= v
            orientation %= 360
        elif h == 'R':
            orientation += v
            orientation %= 360
        elif h == 'F':
            pos = update_pos(pos, headings[orientation], v)
        else:
            pos = update_pos(pos, h, v)

    print(abs(pos[0]) + abs(pos[1]))

def udpate_heading(waypoint, deg):
    if deg == 90:
        return -waypoint[1], waypoint[0]
    elif deg == 180:
        return -waypoint[0], -waypoint[1]
    elif deg == 270:
        return waypoint[1], -waypoint[0]


def part2(filename='input12.txt'):
    directions = [(line[0],int(line[1:])) for line in open(filename, 'r').read().split()]

    ship = (0,0)
    waypoint = (10, -1)

    for h, v in directions:
        if h == 'F':
            ship = ship[0] + (v*waypoint[0]), ship[1]+ (v*waypoint[1])
        elif h == 'L':
            waypoint = udpate_heading(waypoint, 360-v)
        elif h == 'R':
            waypoint = udpate_heading(waypoint, v)
        else:
            waypoint = update_pos(waypoint, h, v)

    print(abs(ship[0]) + abs(ship[1]))

part1()
part2()
