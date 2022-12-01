from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    value = 0
    for i in range(len(data)):
        if data[i] == data[(i + 1) % len(data)]:
            value += int(data[i])
    return value


@function_timer
def part2(data):
    value = 0
    for i in range(len(data)):
        if data[i] == data[(i + len(data)//2) % len(data)]:
            value += int(data[i])
    return value


def main():
    data = get_input(1, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
