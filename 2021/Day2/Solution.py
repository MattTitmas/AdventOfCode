from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    values = [[int(i) if i.isnumeric() else i for i in i.split(" ")] for i in data.split("\n")]

    depth = 0
    horizontal = 0
    for i in values:
        if i[0] == "up":
            depth -= i[1]
        elif i[0] == "down":
            depth += i[1]
        elif i[0] == "forward":
            horizontal += i[1]

    return depth * horizontal


@function_timer_avg
def part2(data):
    values = [[int(i) if i.isnumeric() else i for i in i.split(" ")] for i in data.split("\n")]

    aim = 0
    depth = 0
    horizontal = 0
    for i in values:
        if i[0] == "up":
            aim -= i[1]
        elif i[0] == "down":
            aim += i[1]
        elif i[0] == "forward":
            horizontal += i[1]
            depth += aim * i[1]

    return depth * horizontal


def main():
    data = get_input(2, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
