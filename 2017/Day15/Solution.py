from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer
def part1(data):
    a, b = (int(i.split(' ')[-1]) for i in data.split('\n'))
    factor_a, factor_b = 16807, 48271
    total = 0
    for i in range(40_000_000):
        a = (a * factor_a) % 2147483647
        b = (b * factor_b) % 2147483647
        total += (a & 65535) == (b & 65535)
    return total


@function_timer
def part2(data):
    a, b = (int(i.split(' ')[-1]) for i in data.split('\n'))
    factor_a, factor_b = 16807, 48271
    total = 0
    for i in range(5_000_000):
        a = (a * factor_a) % 2147483647
        while a & 3 != 0:
            a = (a * factor_a) % 2147483647
        b = (b * factor_b) % 2147483647
        while b & 7 != 0:
            b = (b * factor_b) % 2147483647
        total += (a & 65535) == (b & 65535)
    return total


def main():
    data = get_input(15, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
