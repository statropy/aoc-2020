#day9.py

def sumin(pre, v):
    s = set(pre)
    for x in pre:
        if v - x in s and x+x != v:
            return True
    return False

def part1(xmas, preamble=25):
    return [xmas[i] for i in range(preamble, len(xmas)) if not sumin(xmas[i-preamble:i],xmas[i])][0]

def findsum(slice, v):
    s = 0
    for i in range(len(slice)):
        s += slice[i]
        if s == v:
            return slice[:i+1]
        elif s > v:
            return None
    return None

def part2(xmas, v):
    for i in range(len(xmas)):
        f = findsum(xmas[i:], v)
        if f:
            return min(f) + max(f)

if __name__ == '__main__':
    xmas = [int(x) for x in open('input9.txt', 'r')]
    p1 = part1(xmas)
    p2 = part2(xmas,p1)
    print(p1)
    print(p2)
