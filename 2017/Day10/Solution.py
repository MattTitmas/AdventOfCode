from functools import reduce

from aoc import get_input
from utils import function_timer_avg, function_timer
from utils import knot_hash


@function_timer_avg
def part1(data):
    knot = [i for i in range(256)]
    current_position, skip_size = 0, 0
    for i in data.split(','):
        copied_data = knot[:] + knot[:]
        length = int(i)
        copied_data[current_position:current_position + length] = copied_data[current_position:current_position + length][::-1]
        knot = copied_data[0:256]
        if current_position + length > 256:
            knot[:(current_position + length) - 256] = copied_data[256:current_position + length]
        current_position = (current_position + length + skip_size) % 256
        skip_size += 1
    return knot[0] * knot[1]

@function_timer_avg
def part2(data):
    return knot_hash(data)

def main():
    data = get_input(10, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
