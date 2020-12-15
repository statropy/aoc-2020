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

    def test_a(self):
        self.assertEqual(436, number_game([0,3,6]))
    def test_b(self):
        self.assertEqual(1, number_game([1,3,2]))
    def test_c(self):
        self.assertEqual(10, number_game([2,1,3]))
    def test_d(self):
        self.assertEqual(27, number_game([1,2,3]))
    def test_e(self):
        self.assertEqual(78, number_game([2,3,1]))
    def test_f(self):
        self.assertEqual(438, number_game([3,2,1]))
    def test_g(self):
        self.assertEqual(1836, number_game([3,1,2]))
    def test_h(self):
        self.assertEqual(175594, number_game([0,3,6],30000000))

if __name__ == '__main__':
    unittest.main()
