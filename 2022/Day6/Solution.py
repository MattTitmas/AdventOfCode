from aoc import get_input
from utils import function_timer, function_timer_avg


@function_timer_avg
def part1(data):
    n = 4
    for i in range(n - 1, len(data)):
        if len(set(data[i - (n - 1):i + 1])) == n:
            return i + 1


@function_timer_avg
def part2(data):
    n = 14
    for i in range(n - 1, len(data)):
        if len(set(data[i - (n - 1):i + 1])) == n:
            return i + 1


def main():
    data = get_input(6, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
