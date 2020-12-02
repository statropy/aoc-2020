#day2.py

def parse1(line):
    rule, pw = line.split(': ')
    pwrange, char = rule.split(' ')
    ranges = [int(x) for x in pwrange.split('-')]
    minrange, maxrange = int(ranges[0]), int(ranges[1])
    count = pw.count(char)
    return count >= minrange and count <= maxrange

def parse2(line):
    rule, pw = line.split(': ')
    pwrange, char = rule.split(' ')
    ranges = [int(x) for x in pwrange.split('-')]
    return (pw[ranges[0]-1] == char) ^ (pw[ranges[1]-1] == char)

def step():
    with open('input2.txt', 'r') as f:
        correct1 = 0
        correct2 = 0
        for line in f:
            if parse1(line):
                correct1 +=1 
            if parse2(line):
                correct2 += 1
        return correct1, correct2

def combined():
    with open('input2.txt', 'r') as f:
        correct1 = 0
        correct2 = 0
        for line in f:
            rule, pw = line.split(': ')
            pwrange, char = rule.split(' ')
            ranges = [int(x) for x in pwrange.split('-')]
            minrange, maxrange = int(ranges[0]), int(ranges[1])
            count = pw.count(char)
            if count >= minrange and count <= maxrange:
                correct1 += 1
            if (pw[minrange-1] == char) ^ (pw[maxrange-1] == char):
                correct2 += 1
        return correct1, correct2

if __name__ == '__main__':
    print(combined())
