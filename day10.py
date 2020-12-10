#day10.py

def adapt(adapters):
    now = 0
    diff1 = 0
    diff3 = 0
    for x in adapters:
        if x-now == 1:
            diff1 += 1
        if x-now == 3:
            diff3 += 1
        now = x
    return diff1 * (diff3+1)

if __name__ == '__main__':
    adapters = sorted([int(x) for x in open('input10.txt').read().split('\n')])
    print(adapt(adapters))

    d = dict()
    d[adapters[-1]+3] = 1
    adapters.insert(0, 0)

    while len(adapters) > 0:
        last = adapters.pop()
        s = 0
        for i in range(last+1, last+4):
            if i in d.keys():
                s += d[i]
        d[last] = s

    print(d[0])
