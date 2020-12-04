#day4.py
import re

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

def manual():
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



def validate_range(value, minval, maxval, unit=''):
    uval = ''
    if len(unit) > 0:
        value, uval = value[:-len(unit)], value[-len(unit):]
    try:
        ival = int(value)
        return unit == uval and ival >= minval and ival <= maxval
    except Exception:
        return False

def validate_regex(value, *regex):
    return re.compile(''.join(regex)).fullmatch(value) is not None

rules = {'byr': (validate_range, (1920, 2002)),
         'iyr': (validate_range, (2010, 2020)),
         'eyr': (validate_range, (2020, 2030)),
         'hgt': (validate_range, (150, 193, 'cm'), (59, 76, 'in')),
         'hcl': (validate_regex, (r'#[0-9a-f]{6}')),
         'ecl': (validate_regex, (r'amb|blu|brn|gry|grn|hzl|oth')),
         'pid': (validate_regex, (r'[0-9]{9}'))}

def make_passport(fields):
    p = dict([tuple(field.split(':')) for field in fields])
    if p.keys() >= rules.keys():
        return p
    return None

def passport():
    with open('input4.txt', 'r') as f:
        fields = []
        for line in f:
            line = line.strip()
            if len(line) == 0:
                p = make_passport(fields)
                if p: yield p
                fields = []
            else:
                fields += line.split()
        p = make_passport(fields)
        if p: yield p

def is_valid(passport):
    for key,value in passport.items():
        if key in rules.keys():
            func = rules[key][0]
            validators = rules[key][1:]
            valid = [args for args in validators if func(value, *args)]
            if len(valid) == 0:
                return False

    return True

def using_rules():
    present = [p for p in passport()]
    valid  = [p for p in present if is_valid(p)]
    print(len(present), len(valid))

if __name__ == '__main__':
    manual()
    using_rules()
