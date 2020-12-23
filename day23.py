#day23.py

from collections import deque

def step(q):
    current = q[-1]
    store = []
    for i in range(3):
        store.append(q.popleft())
    s = set(store)
    dest = current-1
    if dest == 0: dest = 9
    while dest in s:
        dest -= 1
        if dest == 0: dest = 9
    q.rotate(-q.index(dest)-1)
    q.extend(store)
    q.rotate(-q.index(current)-2)

def play(start, steps=10):
    q = deque([int(x) for x in start])
    #always start with current at the end
    q.rotate(-1)
    for i in range(steps):
        step(q)
    q.rotate(-q.index(1)-1)
    q.pop()
    print(''.join([str(s) for s in q]))

example = '389125467'
start = '364289715'
play(start,100)
