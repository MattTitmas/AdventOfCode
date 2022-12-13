from typing import Tuple, List

from aoc import get_input
from utils import function_timer_avg, function_timer


def get_movements(current_pos: Tuple[int, int], movement: str) -> List[Tuple[int, int]]:
    x, y = current_pos
    if movement[0] == 'U':
        return [(x, y + i) for i in range(1, int(movement[1:]) + 1)]
    elif movement[0] == 'R':
        return [(x + i, y) for i in range(1, int(movement[1:]) + 1)]
    elif movement[0] == 'D':
        return [(x, y - i) for i in range(1, int(movement[1:]) + 1)]
    else:
        return [(x - i, y) for i in range(1, int(movement[1:]) + 1)]


@function_timer
def part1(data):
    paths = []
    for line in data.split('\n'):
        current_path = [(0, 0)]
        for movement in line.split(','):
            current_path += get_movements(current_path[-1], movement)
        paths.append(current_path)

    path_one = paths[0][1:]
    path_two = paths[1][1:]

    intersections = set(path_one).intersection(set(path_two))
    return min([abs(x) + abs(y) for x, y in intersections])



@function_timer
def part2(data):
    paths = []
    for line in data.split('\n'):
        current_path = [(0, 0)]
        for movement in line.split(','):
            current_path += get_movements(current_path[-1], movement)
        paths.append(current_path)

    path_one = paths[0][1:]
    path_two = paths[1][1:]

    intersections = set(path_one).intersection(set(path_two))
    return min([path_one.index((x, y)) + path_two.index((x, y)) + 2 for x, y in intersections])

def main():
    data = get_input(3, 2019)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
