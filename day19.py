#day19_1.py
import re

def makeregex(regex, expr):
    if expr.find('|') == -1:
        return ''.join(['('+regex[int(x)]+')' for x in expr.split(' ')])
    else:
        return '|'.join(['('+makeregex(regex, x)+')' for x in expr.split('|')])

def run(part2=False):
    with open('input19.txt', 'r') as f:
        rules = {}
        msgs = []
        regex = {}
        read_rules = True
        for line in f:
            if len(line) == 1:
                read_rules = False
                continue
            if read_rules:
                rule, expr = line.strip().split(': ')
                rules[int(rule)] = expr.replace('"', '').replace(' | ', '|')

            else:
                msgs.append(line.strip())

        if part2:
            del rules[0]
            del rules[8]
            del rules[11]

        #replace single chars
        single = [(rule,expr) for rule, expr in rules.items() if len(expr) == 1 and expr[0].isalpha()]
        for k,v in single:
            regex[k] = v
            del rules[k]

        #iterative approach
        while len(rules) > 0:
            found = []
            for rule,expr in rules.items():
                tokens = set([int(item) for sublist in [sides.split(' ') for sides in expr.split('|')] for item in sublist])
                if tokens.issubset(regex):
                    newre = makeregex(regex, expr)
                    regex[rule] = newre
                    found.append(rule)

            for k in found:
                del rules[k]

        if part2:
            rule0 = '(?P<left>('+regex[42]+'){2,})' + '(?P<right>('+regex[31]+')+)'
            rule0a = regex[42]
            rule0b = regex[31]
            rega = re.compile(rule0a)
            regb = re.compile(rule0b)
        else:
            rule0 = regex[0]

        count = 0
        reg = re.compile(rule0)

        for msg in msgs:
            m = reg.fullmatch(msg)
            if m:
                if part2:
                    leftside = rega.sub('_', m.group('left'))
                    rightside = regb.sub('_', m.group('right'))
                    if len(leftside) > len(rightside):
                        count += 1
                else:
                    count += 1
        print(count)

run()
run(True)
