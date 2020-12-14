#day14.py
import re

def part1():
    with open('input14.txt', 'r') as f:
        mask_set = 0
        mask_clear = 0
        mask = ''
        mem = {}
        regex = re.compile(r'mem\[(\d+)\] = (\d+)')
        for line in f:
            if line[1] == 'a': #mask
                mask = line[7:].strip()
                mask_set = mask.replace('X', '0')
                mask_clear = mask.replace('X', '1')
                mask_set = int(mask_set, 2)
                mask_clear = int(mask_clear, 2)
            else: #mem
                m = regex.match(line)
                addr, val = [int(v) for v in m.groups()]
                mem[addr] = ((val & mask_clear) | mask_set)
        s = sum(mem.values())
        print(s)

def make_mask(m):
    try:
        if len(m) == 0:
            return ['']
        i = m.index('X')
        prefix = m[:i]
        postfix = m[i+1:]
        return [prefix + bit + substr for bit in ['0', '1'] for substr in make_mask(postfix)]
    except:
        return [m]

def part2():
    with open('input14.txt', 'r') as f:
        mask_clear = 0
        masks = []
        mem = {}
        regex = re.compile(r'mem\[(\d+)\] = (\d+)')
        for line in f:
            if line[1] == 'a': #mask
                mask = line[7:].strip()
                masks = [int(m,2) for m in make_mask(mask)]
                mask_clear = int(mask.replace('0', '1').replace('X', '0'),2)
            else: #mem
                m = regex.match(line)
                addr, val = [int(v) for v in m.groups()]
                addr &= mask_clear
                for m in masks:
                    mem[addr | m] = val
        s = sum(mem.values())
        print(s)

part1()
part2()