#day13.py

def part1(timestamp, schedule):
    departure = {bus-timestamp%bus:bus for bus in schedule}
    waittime = min(departure.keys())
    print(waittime*departure[waittime])

def find_offset(a, offa, b, offb):
    acc = offa
    while True:
        found = True
        if acc % b == offb:
            return acc
        acc += a

def part2(schedule):
    d = {schedule[i]:(schedule[i]-i) % schedule[i] for i in range(len(schedule)) if schedule[i] != 0}
    a = max(d.keys())
    aoff = d[a]

    del d[a]

    z = [(v, d[v]) for v in sorted(list(d),reverse=True)]
    for b, boff in z:
        aoff = find_offset(a, aoff, b, boff)
        a = a*b
    print(aoff)

with open('input13.txt', 'r') as f:
    timestamp = int(next(f).strip())
    schedule = [0 if line == 'x' else int(line) for line in next(f).split(',')]
    part1(timestamp, [bus for bus in schedule if bus > 0])
    part2(schedule)
