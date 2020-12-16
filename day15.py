#day15.py
import unittest

def linear(initial, stop=2020):
    last = 0
    counts = [0]*stop
    for i,v in enumerate(initial):
        counts[v] = i+1
    for turn in range(len(initial)+1, stop):
        v = counts[last]
        counts[last] = turn
        if v == 0:
            last = 0
        else:
            last = turn -v
    return last


def number_game(initial, stop=2020):
    last = 0
    numbers = {v:i+1 for i,v in enumerate(initial)}
    for turn in range(len(initial)+1, stop):
        print(turn, last, len(numbers))
        v = numbers.setdefault(last, 0)
        numbers[last] = turn
        last = 0 if v == 0 else turn - v
    return last

def number_0(initial, stop=2020):
    last = 0
    zero = 0
    numbers = {v:i+1 for i,v in enumerate(initial) if v > 0}
    try:
        zero = initial.index(0)+1
    except:
        pass

    for turn in range(len(initial)+1, stop):
        if last == 0:
            last = turn - zero
            zero = turn
        else:
            v = numbers.setdefault(last, 0)
            numbers[last] = turn
            last = 0 if v == 0 else turn - v
    return last

class TestNumberGame(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(436, number_game([0,3,6]))
        self.assertEqual(1, number_game([1,3,2]))
        self.assertEqual(10, number_game([2,1,3]))
        self.assertEqual(27, number_game([1,2,3]))
        self.assertEqual(78, number_game([2,3,1]))
        self.assertEqual(438, number_game([3,2,1]))
        self.assertEqual(1836, number_game([3,1,2]))
        self.assertEqual(387, number_game([14,1,17,0,3,20]))

    def run_part2(self, f):
        stop = 30000000
        self.assertEqual(175594, f([0,3,6],stop))
        self.assertEqual(2578, f([1,3,2],stop))
        self.assertEqual(3544142, f([2,1,3],stop))
        self.assertEqual(261214, f([1,2,3],stop))
        self.assertEqual(6895259, f([2,3,1],stop))
        self.assertEqual(18, f([3,2,1],stop))
        self.assertEqual(362, f([3,1,2],stop))
        self.assertEqual(6428, f([14,1,17,0,3,20],stop))

    def test_part2_game(self):
        self.run_part2(number_game)

    def test_part2_0(self):
        self.run_part2(number_0)

    def test_part2_linear(self):
        self.run_part2(linear)

    def test_part2(self):
        stop = 30000000
        self.assertEqual(175594, number_game([0,3,6],stop))
        self.assertEqual(2578, number_game([1,3,2],stop))
        self.assertEqual(3544142, number_game([2,1,3],stop))
        self.assertEqual(261214, number_game([1,2,3],stop))
        self.assertEqual(6895259, number_game([2,3,1],stop))
        self.assertEqual(18, number_game([3,2,1],stop))
        self.assertEqual(362, number_game([3,1,2],stop))
        self.assertEqual(6428, number_game([14,1,17,0,3,20],stop))

if __name__ == '__main__':
    #unittest.main()
    print(linear([0,3,6]))
    print(linear([14,1,17,0,3,20],30000000))
