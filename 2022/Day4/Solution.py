from aoc import get_input
from utils import function_timer, function_timer_avg


@function_timer_avg
def part1(data):
    total = 0
    for line in data.split('\n'):
        a, b = line.split(',')
        lower_one, upper_one = (int(i) for i in a.split('-'))
        lower_two, upper_two = (int(i) for i in b.split('-'))
        if (lower_one >= lower_two and upper_one <= upper_two) or (lower_two >= lower_one and upper_two <= upper_one):
            total += 1
    return total


@function_timer_avg
def part2(data):
    total = 0
    for line in data.split('\n'):
        a, b = line.split(',')
        lower_one, upper_one = (int(i) for i in a.split('-'))
        lower_two, upper_two = (int(i) for i in b.split('-'))
        if (upper_one >= lower_two and lower_one <= upper_two) or (upper_two >= lower_one and lower_two <= upper_one):
            total += 1
    return total


def main():
    data = get_input(4, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
