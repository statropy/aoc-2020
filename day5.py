#day5.py

def next_seat():
    with open('input5.txt', 'r') as f:
        for line in f:
            yield(int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2))

if __name__ == '__main__':
    ids = [id for id in next_seat()]
    print(max(ids))
    s = sorted(ids)
    offset = s[0]
    move = len(s) >> 1
    index = move

    while(move > 1):
        move >>= 1
        if s[index] == offset+index:
            index += move
        else:
            index -= move
    print(s[index]+1)
