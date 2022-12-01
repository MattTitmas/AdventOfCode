from collections import Counter

from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    valid_passphrases = 0
    for i in data.split('\n'):
        if len(i.split(' ')) == len(set(i.split(' '))):
            valid_passphrases += 1
    return valid_passphrases


@function_timer
def part2(data):
    valid_passphrases = 0
    for i in data.split('\n'):
        counters = [tuple(sorted(Counter(i).items())) for i in i.split(' ')]
        if len(counters) == len(set(counters)):
            valid_passphrases += 1
    return valid_passphrases


def main():
    data = get_input(4, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
