from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    values = [int(i) for i in data.split(",")]
    amount = dict((x, values.count(x)) if x in values else (x, 0) for x in range(0, 9))
    for i in range(80):
        numberZero = amount[0]
        for j in range(0, 8):
            amount[j] = amount[j + 1]
        amount[6] += numberZero
        amount[8] = numberZero
    return sum(amount.values())


@function_timer_avg
def part2(data):
    values = [int(i) for i in data.split(",")]
    amount = dict((x, values.count(x)) if x in values else (x, 0) for x in range(0, 9))
    for i in range(256):
        numberZero = amount[0]
        for j in range(0, 8):
            amount[j] = amount[j + 1]
        amount[6] += numberZero
        amount[8] = numberZero
    return sum(amount.values())


def main():
    data = get_input(6, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
