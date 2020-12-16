#day16.py

def part1(fields, nearby):
    invalid = 0
    for ticket in nearby:
        for v in ticket:
            addto = True
            for valid in fields.values():
                if v in valid:
                    addto = False
                    break
            if addto:
                invalid += v
                break
    return invalid

def valid_ticket(fields, ticket):
    for v in ticket:
        isvalid = False
        for valid in fields.values():
            if v in valid:
                isvalid = True
                break
        if not isvalid:
            return False
    return True

def couldbe(field, column, fields, nearby):
    for t in nearby:
        if t[column] not in fields[field]:
            return False
    return True

def iterate_remaining(fieldstoplace, fields, nearby):
    fieldstoexclude = {k:[] for k in fieldstoplace.keys()}
    for field in fieldstoplace.keys():
        for col in fieldstoplace[field]:
            if not couldbe(field, col, fields, nearby):
                #fieldstoplace[field].remove(col)
                fieldstoexclude[field].append(col)
                #print(field, 'not in col', col)
    return fieldstoexclude


def part2(fields, ticket, nearby):
    nearby = [t for t in nearby if valid_ticket(fields, t)]

    fieldstoplace = {k:set(range(len(ticket))) for k in fields.keys()}
    found = {}

    while len(found) < len(ticket):
        #print('FTP:', fieldstoplace)
        ex = iterate_remaining(fieldstoplace, fields, nearby)
        #print('Exclude:', ex)
        for field in ex:
            for v in ex[field]:
                fieldstoplace[field].remove(v)
            if len(fieldstoplace[field]) == 1:
                colfound = fieldstoplace[field].pop()
                found[field] = colfound
                del fieldstoplace[field]
                for f in fieldstoplace:
                    fieldstoplace[f].remove(colfound)
        print('Found:',found)
    prod = 1
    for field in [field for field in fields.keys() if field[:9] == 'departure']:
        prod *= ticket[found[field]]
    return prod

with open('input16.txt', 'r') as f:
    state = 0
    fields = {}
    ticket = []
    nearby = []
    for line in f:
        line = line.strip()
        if len(line) == 0:
            state += 1
        elif state == 0:
            field, values = line.split(':')
            values = [v.strip() for v in values.split('or')]
            values = [v.split('-') for v in values]
            values = [set(range(int(low),int(high)+1)) for low, high in values]
            values = {v for sublist in values for v in sublist}
            fields[field] = values
            #print(field, values)
        elif state == 1:
            if line == 'your ticket:':
                state += 1
        elif state == 2:
            ticket = [int(v) for v in line.split(',')]
            #print(ticket)
        elif state == 3:
            if line == 'nearby tickets:':
                state += 1
        elif state == 4:
            nearby.append([int(v) for v in line.split(',')])
    #print(nearby)

    print(part1(fields, nearby))
    print(part2(fields, ticket, nearby))