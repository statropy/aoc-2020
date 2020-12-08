#day8.py

def part1(program):
    pc = 0
    acc = 0
    visited = [0]*len(program)
    while visited[pc] == 0:
        visited[pc] = 1
        inst, value = program[pc]
        if inst == 'jmp':
            pc += value
        else:
            if inst == 'acc':
                acc += value
            pc += 1
    print(acc)

def terminator(program, swap):
    pc = 0
    acc = 0
    visited = [0]*len(program)

    while pc < len(program):
        if visited[pc] == 1:
            return None

        visited[pc] = 1
        inst, value = program[pc]

        if pc == swap:
            if inst == 'jmp':
                inst = 'nop';
            else:
                inst = 'jmp'

        if inst == 'jmp':
            pc += value
        else:
            if inst == 'acc':
                acc += value
            pc += 1
    return acc

if __name__ == '__main__':
    program = [[int(v) if v[-1].isdigit() else v for v in line.split()] for line in open('input8.txt', 'r')]
    part1(program)
    for pc in range(len(program)):
        if program[pc][0] != 'acc':
            x = terminator(program, pc)
            if x is not None:
                print(x)
                break
