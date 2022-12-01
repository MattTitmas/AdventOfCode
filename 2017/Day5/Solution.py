from collections import Counter

from numba import jit
from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer
def part1(data):
    data = list(map(lambda x: int(x), data.split('\n')))
    count = 0
    position = 0
    while position < len(data):
        data[position], position = data[position] + 1, position + data[position]
        count += 1
    return count


@function_timer
def part2(data):
    data = list(map(lambda x: int(x), data.split('\n')))
    count = 0
    position = 0
    while position < len(data):
        jumps = data[position]
        if jumps >= 3:
            data[position] -= 1
        else:
            data[position] += 1
        position += jumps
        count += 1
    return count


def main():
    data = get_input(5, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
