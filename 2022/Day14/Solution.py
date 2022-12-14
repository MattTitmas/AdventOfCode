from typing import List

from aoc import get_input
from utils import function_timer, function_timer_avg


@function_timer_avg
def part1(data):
    rock_positions = set()
    abyss_y = 0
    for line in data.split('\n'):
        steps = list(map(lambda s: tuple(map(int, s.split(','))), line.split(' -> ')))
        for i in range(1, len(steps)):
            delta_x = steps[i][0] - steps[i - 1][0]
            delta_y = steps[i][1] - steps[i - 1][1]
            abyss_y = max(abyss_y, steps[i - 1][1], steps[i][1])
            if delta_x == 0:
                for j in range(0, delta_y + (-1 if delta_y < 0 else 1), (-1 if delta_y < 0 else 1)):
                    rock_positions.add((steps[i][0], steps[i - 1][1] + j))
            else:
                for j in range(0, delta_x + (-1 if delta_x < 0 else 1), (-1 if delta_x < 0 else 1)):
                    rock_positions.add((steps[i - 1][0] + j, steps[i - 1][1]))

    path = [(500, 0)]
    sand_falling = True
    sand = 0
    while sand_falling:
        still_moving = True
        x, y = path.pop()
        while still_moving:
            if y > abyss_y:
                return sand
            path.append((x, y))
            if (x, y + 1) not in rock_positions:
                y += 1
            elif (x - 1, y + 1) not in rock_positions:
                y += 1
                x -= 1
            elif (x + 1, y + 1) not in rock_positions:
                y += 1
                x += 1
            else:
                still_moving = False
        rock_positions.add((x, y))
        sand += 1
        path.pop()
    return sand



@function_timer_avg
def part2(data):
    rock_positions = set()
    abyss_y = 0
    for line in data.split('\n'):
        steps = list(map(lambda s: tuple(map(int, s.split(','))), line.split(' -> ')))
        for i in range(1, len(steps)):
            delta_x = steps[i][0] - steps[i - 1][0]
            delta_y = steps[i][1] - steps[i - 1][1]
            abyss_y = max(abyss_y, steps[i - 1][1], steps[i][1])
            if delta_x == 0:
                for j in range(0, delta_y + (-1 if delta_y < 0 else 1), (-1 if delta_y < 0 else 1)):
                    rock_positions.add((steps[i][0], steps[i - 1][1] + j))
            else:
                for j in range(0, delta_x + (-1 if delta_x < 0 else 1), (-1 if delta_x < 0 else 1)):
                    rock_positions.add((steps[i - 1][0] + j, steps[i - 1][1]))

    path = [(500, 0)]
    sand_falling = True
    sand = 0
    while sand_falling:
        still_moving = True
        x, y = path.pop()
        while still_moving:
            if y == abyss_y + 1:
                still_moving = False
                rock_positions.add((x, y))
                continue
            path.append((x, y))
            if (x, y + 1) not in rock_positions:
                y += 1
            elif (x - 1, y + 1) not in rock_positions:
                y += 1
                x -= 1
            elif (x + 1, y + 1) not in rock_positions:
                y += 1
                x += 1
            else:
                still_moving = False
        rock_positions.add((x, y))
        sand += 1
        if (x, y) == (500, 0):
            return sand
        path.pop()
    return sand




def main():
    data = get_input(14, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
