import itertools

from aoc import get_input
from utils import function_timer_avg, function_timer


def scanner(height, time):
    offset = time % ((height - 1) * 2)

    return 2 * (height - 1) - offset if offset > height - 1 else offset

@function_timer
def part1(data):
    lines = [line.split(': ') for line in data.split('\n')]

    heights = {int(pos): int(height) for pos, height in lines}
    return sum(pos * heights[pos] for pos in heights if scanner(heights[pos], pos) == 0)


@function_timer
def part2(data):
    lines = [line.split(': ') for line in data.split('\n')]

    heights = {int(pos): int(height) for pos, height in lines}
    return next(wait for wait in itertools.count() if not any(scanner(heights[pos], wait + pos) == 0 for pos in heights))

def main():
    data = get_input(13, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
