#input7.py
import re

def children(d, color):
    total = 0
    for count, child in d[color]:
        total += int(count) + int(count)*children(d, child)
    return total

def part2():
    regex = re.compile(r'(\d+) (\w+ \w+) bag[s]?')
    bagdict = {}
    with open('input7.txt', 'r') as f:
        for line in f:
            bag, inner = line.strip()[:-1].split(' bags contain ')
            if inner == 'no other bags':
                bagdict[bag] = []
            else:
                bagdict[bag] = [re.match(regex, a.strip()).group(1,2) for a in inner.split(',')]
        print(children(bagdict, 'shiny gold'))

def parents(d, color, found):
    if color in d.keys():
        for (parent, count) in d[color]:
            found.add(parent)
            parents(d, parent, found)

def part1():
    regex = re.compile(r'(\d+) (\w+ \w+) bag[s]?')
    bagdict = {}
    with open('input7.txt', 'r') as f:
        for line in f:
            parent, inner = line.strip()[:-1].split(' bags contain ')
            if inner == 'no other bags':
                pass
            else:
                for innerbag in inner.split(','):
                    count, color =  re.match(regex, innerbag.strip()).group(1,2)
                    count = int(count)
                    if color in bagdict.keys():
                        bagdict[color].append((parent, count))
                    else:
                        bagdict[color] = [(parent, count)]
        p = set()
        parents(bagdict, 'shiny gold', p)
        print(len(p))

if __name__ == '__main__':
    part1()
    part2()
