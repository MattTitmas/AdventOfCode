from utils import function_timer
from aoc import get_input


@function_timer
def part1(data):
    return max([sum(i) for i in data])


@function_timer
def part2(data):
    summed_data = [sum(i) for i in data]
    value_one = max(summed_data)
    summed_data.remove(value_one)
    value_two = max(summed_data)
    summed_data.remove(value_two)
    value_three = max(summed_data)
    summed_data.remove(value_three)
    return value_three + value_two + value_one


def main():
    data = get_input(1, 2022)
    data = [[int(j) for j in i.split('\n')] for i in data.split('\n\n')]
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
