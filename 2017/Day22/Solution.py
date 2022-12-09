from math import sin, cos, radians

from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer
def part1(data):
    infected = set()
    max_j = len(data.split('\n'))
    max_i = len(data.split('\n')[0])
    for count_j, j in enumerate(data.split('\n')):
        for count_i, i in enumerate(j):
            if i == '#':
                infected.add((count_i, count_j))
    x, y, angle = int(max_i // 2), int(max_j // 2), 0

    caused_infection = 0
    for _ in range(10000):
        if (x, y) in infected:
            angle += 90
            infected.remove((x, y))
        else:
            caused_infection += 1
            angle -= 90
            infected.add((x, y))
        angle %= 360
        change_x, change_y = int(sin(radians(angle))), -int(cos(radians(angle)))
        x += change_x
        y += change_y
    return caused_infection




@function_timer
def part2(data):
    infected = set()
    weakened = set()
    flagged = set()
    max_j = len(data.split('\n'))
    max_i = len(data.split('\n')[0])
    for count_j, j in enumerate(data.split('\n')):
        for count_i, i in enumerate(j):
            if i == '#':
                infected.add((count_i, count_j))
    x, y, angle = int(max_i // 2), int(max_j // 2), 0

    caused_infection = 0
    for _ in range(10_000_000):
        if (x, y) in infected:
            angle += 90
            infected.remove((x, y))
            flagged.add((x, y))
        elif (x, y) in weakened:
            weakened.remove((x, y))
            caused_infection += 1
            infected.add((x, y))
        elif (x, y) in flagged:
            angle += 180
            flagged.remove((x, y))
        else:
            angle -= 90
            weakened.add((x, y))
        angle %= 360
        change_x, change_y = int(sin(radians(angle))), -int(cos(radians(angle)))
        x += change_x
        y += change_y
    return caused_infection


def main():
    data = get_input(22, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
