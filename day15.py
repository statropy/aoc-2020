#day15.py
import unittest

def number_game(initial, stop=2020):
    last = 0
    numbers = {v:i+1 for i,v in enumerate(initial)}
    for turn in range(len(initial)+1, stop):
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
    unittest.main()
