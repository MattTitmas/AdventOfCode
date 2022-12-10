from collections import defaultdict

from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer
def part1(data):
    rules = dict()
    split_data = data.split('\n')[3:]
    state = data.split('\n')[0].split(' ')[-1][:-1]
    number_of_steps = int(data.split('\n')[1].split(' ')[-2])
    for i in range(0, len(split_data), 10):
        line = split_data[i]
        state = line.split(' ')[-1][:-1]
        zero = int(split_data[i+2].split(' ')[-1][:-1]), 1 if split_data[i+3].split(' ')[-1][:-1] == 'right' else -1, split_data[i+4].split(' ')[-1][:-1]
        one = int(split_data[i+6].split(' ')[-1][:-1]), 1 if split_data[i+7].split(' ')[-1][:-1] == 'right' else -1, split_data[i+8].split(' ')[-1][:-1]
        rules[state] = {
            0: zero,
            1: one
        }
    slots = defaultdict(int)
    slot = 0

    for i in range(number_of_steps):
        commands = rules[state][slots[slot]]
        slots[slot] = commands[0]
        slot += commands[1]
        state = commands[2]
    return sum(slots.values())





@function_timer
def part2(data):
    return None


def main():
    data = get_input(25, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
