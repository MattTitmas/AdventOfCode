from functools import reduce

from aoc import get_input
from utils import function_timer_avg, function_timer


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
    ascii_characters = [ord(c) for c in data] + [17, 31, 73, 47, 23]
    knot = [i for i in range(256)]
    current_position, skip_size = 0, 0
    for j in range(64):
        for i in ascii_characters:
            copied_data = knot[:] + knot[:]
            length = int(i)
            copied_data[current_position:current_position + length] = copied_data[current_position:current_position + length][::-1]
            knot = copied_data[0:256]
            if current_position + length > 256:
                knot[:(current_position + length) - 256] = copied_data[256:current_position + length]
            current_position = (current_position + length + skip_size) % 256
            skip_size += 1

    return "".join(["{:02x}".format(reduce(lambda x, y: x ^ y, knot[i:i+16])) for i in range(0,256,16)])

def main():
    data = get_input(10, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
