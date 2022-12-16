import re

from aoc import get_input
from utils import function_timer, function_timer_avg


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def abcd2abr(a, b, c, d):
    return a, b, dist((a, b), (c, d))


@function_timer_avg
def part1(data):
    data = [abcd2abr(*map(int, re.findall(r'[-]*\d+', line)))
            for line in data.split("\n")]
    intervals = sorted([(x - d, x + d) for x, y, r in data for d in [r - abs(2_000_000 - y)] if d >= 0])
    return max([b for _, b in intervals]) - intervals[0][0]


@function_timer_avg
def part2(data):
    data = [abcd2abr(*map(int, re.findall(r'[-]*\d+', line)))
            for line in data.split("\n")]
    intervals = sorted([(x - d, x + d) for x, y, r in data for d in [r - abs(2_000_000 - y)] if d >= 0])

    start, stop, holes = *intervals[0], 0

    for nstart, nstop in intervals:
        holes, stop = max(0, nstart - stop - 1), max(stop, nstop)

    a = set(x - y + r + 1 for x, y, r in data).intersection(x - y - r - 1 for x, y, r in data).pop()
    b = set(x + y + r + 1 for x, y, r in data).intersection(x + y - r - 1 for x, y, r in data).pop()

    return (a + b) * 2_000_000 + (b - a) // 2


def main():
    data = get_input(15, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
