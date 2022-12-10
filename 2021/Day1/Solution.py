from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    values = [int(i) for i in data.split("\n")]
    return sum([1 if values[i] > values[i - 1] else 0 for i in range(len(values))])


@function_timer_avg
def part2(data):
    values = [int(i) for i in data.split("\n")]
    return sum(
        [1 if values[i + 1] + values[i + 2] > values[i - 1] + values[i + 1] else 0 for i in range(1, len(values) - 2)])


def main():
    data = get_input(1, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
