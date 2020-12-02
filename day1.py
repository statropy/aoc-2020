#day1.py

def step1():
    with open('input1.txt', 'r') as f:
        expenses = set()
        for line in f:
            amount = int(line)
            match = 2020 - amount
            if match in expenses:
                return amount, match, amount * match
            expenses.add(amount)

def step2():
    with open('input1.txt', 'r') as f:
        expenses = set()
        for line in f:
            amount = int(line)
            for second in expenses:
                match = 2020 - amount - second
                if match in expenses:
                    return amount * second * match
            expenses.add(amount)

if __name__ == '__main__':
    print(step1())
    print(step2())
    with open('input1.txt', 'r') as f:
        expenses = [int(line) for line in f]
        print([x*y for y in expenses for x in expenses if x+y==2020][0])
