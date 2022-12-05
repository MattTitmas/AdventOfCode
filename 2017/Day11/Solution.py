from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer
def part1(data):
    steps = data.split(',')
    rules = {
        'n': [('z', -1), ('y', 1)],
        's': [('z', 1), ('y', -1)],
        'nw': [('x', -1), ('y', 1)],
        'ne': [('z', -1), ('x', 1)],
        'sw': [('x', -1), ('z', 1)],
        'se': [('y', -1), ('x', 1)],
    }
    positions = {
        'x': 0, 'y': 0, 'z': 0
    }
    for command in steps:
        for a, b in rules[command]:
            positions[a] += b
    return sum([abs(i) for i in list(positions.values())]) // 2


@function_timer
def part2(data):
    steps = data.split(',')
    rules = {
        'n': [('z', -1), ('y', 1)],
        's': [('z', 1), ('y', -1)],
        'nw': [('x', -1), ('y', 1)],
        'ne': [('z', -1), ('x', 1)],
        'sw': [('x', -1), ('z', 1)],
        'se': [('y', -1), ('x', 1)],
    }
    positions = {
        'x': 0, 'y': 0, 'z': 0
    }
    max_so_far = -1
    for command in steps:
        for a, b in rules[command]:
            positions[a] += b
        max_so_far = max(max_so_far, sum([abs(i) for i in list(positions.values())]) // 2)
    return max_so_far


def main():
    data = get_input(11, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
