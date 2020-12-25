#day25.py

def run(sn, pk, maxruns=100000000):
    n = 1
    for i in range(maxruns):
        n = (n*sn) % 20201227
        if n == pk:
            return i+1
    return 0

def unlock(sn, runs):
    n = 1
    for i in range(runs):
        n = (n*sn) % 20201227
    return n

def part1(card, door, sn=7):
    card_loops = run(sn, card)
    door_loops = run(sn, door)
    print(card_loops, door_loops)
    if card_loops < door_loops:
        return unlock(door, card_loops)
    else:
        return unlock(card, door_loops)

card_pk = 2959251
door_pk = 4542595

print(part1(card_pk, door_pk))