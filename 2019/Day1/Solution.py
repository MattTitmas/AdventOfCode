from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    return sum([int(i) // 3 - 2 for i in data.split('\n')])


@function_timer_avg
def part2(data):
    total_fuel = 0
    for fuel in data.split('\n'):
        fuel = int(fuel) // 3 - 2
        while fuel > 0:
            total_fuel += fuel
            fuel = fuel // 3 - 2
    return total_fuel


def main():
    data = get_input(1, 2019)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
