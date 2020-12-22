#day22.py
def calcscore(deck):
    size = len(deck)
    return sum([c * (size - i) for i, c in enumerate(deck)])

def combat(deck1, deck2):
    rounds = 0
    while rounds < 1000:
        rounds += 1
        if len(deck1) == 0:
            print(calcscore(deck2))
            return
        elif len(deck2) == 0:
            print(calcscore(deck1))
            return
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        if c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        elif c2 > c1:
            deck2.append(c2)
            deck2.append(c1)
    print('Part 1 overflow')

def rcombat(deck1, deck2, depth=0):
    states = set()
    rounds = 0
    while True:
        rounds += 1
        state = (tuple(deck1), tuple(deck2))
        if state in states:
            deck2 = []
        else:
            states.add(state)
        rounds += 1
        if len(deck1) == 0:
            return 2, calcscore(deck2) if depth==0 else 0
        elif len(deck2) == 0:
            return 1, calcscore(deck1) if depth==0 else 0
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        w = 0
        if len(deck1) >= c1 and len(deck2) >= c2:
            w, score = rcombat(deck1[:c1], deck2[:c2], depth+1)
        else:
            w = 1 if c1 > c2 else 2

        if w == 1:
            deck1.append(c1)
            deck1.append(c2)
        else:
            deck2.append(c2)
            deck2.append(c1)
    print('Part 2 overflow')
    return 1,-2

deck1 = []
deck2 = []
d = deck1
with open('input22.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == 'P':
            if line[7] == '1':
                d = deck1
            else:
                d = deck2
        else:
            d.append(int(line))

combat(deck1[:], deck2[:])
print(rcombat(deck1, deck2))

