#day18.py
import unittest

def get_left(s, part2=False):
    if len(s) == 0:
        return None
    if s[0] == '(':
        depth = 1
        for i in range(1,len(s)):
            if s[i] == '(':
                depth += 1
            elif s[i] == ')':
                depth -= 1
                if depth == 0:
                    return evaluate(s[1:i], part2), s[i+1:]
    else: #should be a number...
        for i in range(1, len(s)):
            if s[i] not in '0123456789':
                return int(s[:i]), s[i:]
        return int(s), None

def operate(left, right, part2=False):
    op, right = right[0], right[1:]
    if part2:
        if op == '+':
            right, remaining = get_left(right, part2)
            return left + right, remaining
        else:
            return left * evaluate(right, part2), None
    else:
        right, remaining = get_left(right, part2)
        if op == '+':
            return left + right, remaining
        else:
            return left * right, remaining

def evaluate(s, part2=False):
    left, remaining = get_left(s, part2)
    while remaining and len(remaining) > 0:
        if remaining is None:
            return left
        left, remaining = operate(left, remaining, part2)
    return left

def math1(s):
    return evaluate(s.strip().replace(' ', ''))

def math2(s):
    return evaluate(s.strip().replace(' ', ''), True)

def run(f):
    return sum([f(line) for line in open('input18.txt', 'r')])

class TestMath(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(10, math1('2 * 3 + 4'))
        self.assertEqual(71, math1('1 + 2 * 3 + 4 * 5 + 6'))
        self.assertEqual(51, math1('1 + (2 * 3) + (4 * (5 + 6))'))
        self.assertEqual(26, math1('2 * 3 + (4 * 5)'))
        self.assertEqual(437, math1('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
        self.assertEqual(12240, math1('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
        self.assertEqual(13632, math1('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))

    def test_part2(self):
        self.assertEqual(14, math2('2 * 3 + 4'))
        self.assertEqual(231, math2('1 + 2 * 3 + 4 * 5 + 6'))
        self.assertEqual(51, math2('1 + (2 * 3) + (4 * (5 + 6))'))
        self.assertEqual(46, math2('2 * 3 + (4 * 5)'))
        self.assertEqual(1445, math2('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
        self.assertEqual(669060, math2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
        self.assertEqual(23340, math2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))

#unittest.main()
print(run(math1))
print(run(math2))
