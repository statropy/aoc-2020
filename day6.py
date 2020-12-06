#day6.py
import functools

if __name__ == '__main__':
    print(sum([len(set(a.replace('\n', ''))) for a in open('input6.txt', 'r').read().split('\n\n')]))
    
    print(sum([len(functools.reduce(lambda x, y: x | y, [set(b) for b in a.split('\n')])) for a in open('input6.txt', 'r').read().split('\n\n')]))
    print(sum([len(functools.reduce(lambda x, y: x & y, [set(b) for b in a.split('\n')])) for a in open('input6.txt', 'r').read().split('\n\n')]))
