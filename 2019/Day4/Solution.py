from typing import Tuple, List

from aoc import get_input
from utils import function_timer_avg, function_timer


def ascending(to_check: str):
    return all(c1 <= c2 for c1, c2 in zip(to_check, to_check[1:]))


def repeated(to_check: str):
    current = to_check[0]
    for i in to_check[1:]:
        if current == i:
            return True
        current = i
    return False


def repeated_two(to_check: str):
    current = to_check[0]
    count = 1
    for i in to_check[1:]:
        if i != current:
            if count == 2:
                return True
            current = i
            count = 1
        else:
            count += 1

    return count == 2


@function_timer_avg
def part1(data):
    total = 0
    lower_bound, upper_bound = tuple(data.split('-'))
    number = list([int(i) for i in lower_bound])
    while int(''.join(map(str, number))) <= int(upper_bound):
        for i in range(5, -1, -1):
            number[i] += 1
            if number[i] != 10:
                break

            if i == 0:
                number[i] = 0
            else:
                number[i] = number[i - 1]
        str_value = ''.join(map(str, number))
        total += (ascending(str_value) and repeated(str_value))
    return total


@function_timer_avg
def part2(data):
    total = 0
    lower_bound, upper_bound = tuple(data.split('-'))
    number = list([int(i) for i in lower_bound])
    while int(''.join(map(str, number))) <= int(upper_bound):
        for i in range(5, -1, -1):
            number[i] += 1
            if number[i] != 10:
                break

            if i == 0:
                number[i] = 0
            else:
                number[i] = number[i - 1]
        str_value = ''.join(map(str, number))
        total += (ascending(str_value) and repeated_two(str_value))
    return total


def main():
    data = get_input(4, 2019)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
