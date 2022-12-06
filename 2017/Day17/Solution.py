from collections import deque

from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    current_position = 0
    values = [0]
    for i in range(2017):
        current_position = ((current_position + (int(data) % (i + 1))) % (i + 1)) + 1
        values.insert(current_position, i+1)
    return values[values.index(2017)+1]


@function_timer
def part2(data):
    current_position = 0
    val_after_zero = -1
    for i in range(50_000_000):
        current_position = ((current_position + (int(data) % (i + 1))) % (i + 1)) + 1
        if current_position == 1:
            val_after_zero = i + 1
    return val_after_zero


def main():
    data = get_input(17, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
