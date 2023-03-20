from aoc import get_input
from utils import function_timer_avg, function_timer

from collections import Counter


@function_timer_avg
def part1(data):
    counted_data = Counter(data)
    return counted_data['('] - counted_data[')']


@function_timer_avg
def part2(data):
    floor = 0
    for count, char in enumerate(data):
        floor += 1 if char == '(' else -1
        if floor == -1:
            return count + 1


def main():
    data = get_input(1, 2015)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
