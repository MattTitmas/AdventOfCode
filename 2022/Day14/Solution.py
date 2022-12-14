from typing import List

from aoc import get_input
from utils import function_timer, function_timer_avg


@function_timer
def part1(data):
    width, height = 90, 180
    grid = [['.'] * width for _ in range(height)]

    abyss_y = 0
    for line in data.split('\n'):
        steps = list(map(lambda s: list(map(int, s.split(','))), line.split(' -> ')))
        for (x, y), (dest_x, dest_y) in zip(steps, steps[1:]):
            while True:
                grid[y][x - 460] = '#'

                if x != dest_x:
                    x += 1 if x < dest_x else -1
                elif y != dest_y:
                    y += 1 if y < dest_y else -1
                else:
                    break
                if y > abyss_y:
                    abyss_y = y

    path = [(500-460, 0)]
    sand_falling = True
    sand = 0
    while sand_falling:
        still_moving = True
        x, y = path.pop()
        while still_moving:
            if y > abyss_y:
                sand -= 1
                still_moving = False
                sand_falling = False
            path.append((x, y))
            if grid[y + 1][x] == '.':
                y += 1
            elif grid[y + 1][x - 1] == '.':
                y += 1
                x -= 1
            elif grid[y + 1][x + 1] == '.':
                y += 1
                x += 1
            else:
                still_moving = False
        grid[y][x] = 'O'
        sand += 1
        path.pop()
    return sand


@function_timer
def part2(data):
    width, height = 500, 180
    grid = [['.'] * width for _ in range(height)]

    translate_x = lambda x: x - 460

    abyss_y = 0
    for line in data.split('\n'):
        steps = list(map(lambda s: list(map(int, s.split(','))), line.split(' -> ')))
        for (x, y), (dest_x, dest_y) in zip(steps, steps[1:]):
            while True:
                grid[y][translate_x(x)] = '#'

                if x != dest_x:
                    x += 1 if x < dest_x else -1
                elif y != dest_y:
                    y += 1 if y < dest_y else -1
                else:
                    break
            abyss_y = max(abyss_y, y, dest_y)

    path = [(500-460, 0)]
    sand_falling = True
    sand = 0
    while sand_falling:
        still_moving = True
        x, y = path.pop()
        while still_moving:
            path.append((x, y))
            if y == abyss_y + 1:
                still_moving = False
            elif grid[y + 1][x] == '.':
                y += 1
            elif grid[y + 1][x - 1] == '.':
                y += 1
                x -= 1
            elif grid[y + 1][x + 1] == '.':
                y += 1
                x += 1

            else:
                still_moving = False
        grid[y][x] = 'O'
        sand += 1
        path.pop()

        if (x, y) == (40, 0):
            sand_falling = False

    return sand




def main():
    data = get_input(14, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
