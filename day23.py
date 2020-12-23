#day23.py

from collections import deque

def step(q):
    current = q[-1]
    store = []
    for i in range(3):
        store.append(q.popleft())
    s = set(store)
    dest = current-1
    if dest == 0: dest = len(q)+3
    while dest in s:
        dest -= 1
        if dest == 0: dest = len(q)+3
    q.rotate(-q.index(dest)-1)
    q.extend(store)
    q.rotate(-q.index(current)-2)

def play1(start, steps=10):
    q = deque([int(x) for x in start])
    #always start with current at the end
    q.rotate(-1)
    for i in range(steps):
        step(q)
    q.rotate(-q.index(1)-1)
    q.pop()
    print(''.join([str(s) for s in q]))

def part2(start, steps=10, elements=100):
    first = None
    nine = None
    one = None

    cup, cuplist = int(start[0]), [int(x) for x in start[1:]]
    n = Node(cup)
    first = n

    for cup in cuplist:
        n = n.insert_cup(cup)
        if cup == 9:
            nine = n
        elif cup == 1:
            one = n

    one.dest = nine
    x = one
    for cup in range(2,10):
        z = n.findcup(cup)
        z.dest = x
        x = z

    n = n.insert_cup(10, nine)
    for cup in range(11, elements+1):
        n = n.insert_cup(cup, n)
        
    one.dest = n

    current = first

    for i in range(steps):
        removed = current.take3()
        s = {removed.cup, removed.next.cup, removed.next.next.cup}
        dest = current.finddest(s)
        dest.insert3(removed)
        current = current.next

    print(one.next.cup * one.next.next.cup)

class Node:
    def __init__(self, cup=0, last=None, next=None, dest=None):
        self.cup = cup
        if last is None:
            last = self
        if next is None:
            next = self
        self.last = last
        self.next = next
        self.dest = dest

    def insert_cup(self, cup, dest=None):
        n = Node(cup, self, self.next)
        self.next.last = n
        self.next = n
        n.dest = dest
        return n

    def take3(self):
        head_removed = self.next
        new_next = self.next.next.next.next
        self.next = new_next
        new_next.last = self
        return head_removed

    def insert3(self, chain):
        new_tail = self.next
        self.next = chain
        chain.last = self
        chain.next.next.next = new_tail
        new_tail.last = chain.next.next

    def finddest(self, exclude):
        d = self.dest
        while d.cup in exclude:
            d = d.dest
        return d

    def findcup(self, cup):
        n = self
        while n.cup != cup:
            n = n.next
        return n

    def __repr__(self):
        return '%d->%d->%d (%d)' % (self.last.cup, self.cup, self.next.cup, self.dest.cup)

example = '389125467'
start = '364289715'
play1(start,100)
part2(start, steps=10000000, elements=1000000)
