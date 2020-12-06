#day5.py

def next_seat():
    with open('input5.txt', 'r') as f:
        for line in f:
            yield(int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2))

def first_way():
    ids = [id for id in next_seat()]
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
    print(s[-1], s[index]+1)

def golf():
    seats = [int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2) for line in open('input5.txt', 'r')]
    print(max(seats),[seat for seat in range(max(seats), min(seats), -1) if seat not in seats][0])

def efficient():
    seatmap = [0]*1024
    max_id = 0
    with open('input5.txt', 'r') as f:
        for line in f:
            id = int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)
            max_id = max(id, max_id)
            seatmap[id] = 1
        for i in range(max_id-1, 0, -1):
            if seatmap[i] == 0:
                print(max_id, i)
                break

if __name__ == '__main__':
    first_way()
    golf()
    efficient()
