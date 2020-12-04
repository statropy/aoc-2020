#day4.py
def process(passport):
    if len(passport) < 7:
        return False, False
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    d = {}
    for f in passport:
        key, value = f.split(':')
        d[key] = value
    for f in fields:
        if f not in d.keys():
            return False, False

    try:
        byr = int(d['byr'])
        if byr < 1920 or byr > 2002: raise Exception

        iyr = int(d['iyr'])
        if iyr < 2010 or iyr > 2020: raise Exception

        eyr = int(d['eyr'])
        if eyr < 2020 or eyr > 2030: raise Exception

        hgt = int(d['hgt'][:-2])
        hunit = d['hgt'][-2:]
        if hunit == 'cm':
            if hgt < 150 or hgt > 193: raise Exception
        elif hunit == 'in':
            if hgt < 59 or hgt > 76: raise Exception
        else:
            raise Exception

        if d['hcl'][0] != '#': raise Exception
        hcl = d['hcl'][1:]
        if len(hcl) != 6: raise Exception
        for c in hcl:
            if c not in '0123456789abcdef': raise Exception

        if d['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: raise Exception

        if len(d['pid']) != 9: raise Exception
        for c in d['pid']:
            if c not in '0123456789': raise Exception

    except Exception as e:
        return True, False

    return True, True

if __name__ == '__main__':
    with open('input4.txt', 'r') as f:
        present = 0
        valid = 0
        fields = []
        for line in f:
            line = line.strip()
            if len(line) == 0:
                p,v = process(fields)
                if p: present += 1
                if v: valid += 1 
                fields = []
            else:
                fields += line.split()
        p,v = process(fields)
        if p: present += 1
        if v: valid += 1 
        print(present, valid)
