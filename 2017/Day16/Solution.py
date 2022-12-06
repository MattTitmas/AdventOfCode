from collections import deque

from aoc import get_input
from utils import function_timer_avg, function_timer


def dance(current_order, data):
    values = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
              'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15}
    values_reversed = {v: k for k, v in values.items()}
    items = deque([values[i] for i in current_order])
    for command in data.split(','):
        if command[0] == 's':
            items.rotate(int(command[1:]))
        elif command[0] == 'x':
            a, b = tuple(map(int, command[1:].split('/')))
            items[a], items[b] = items[b], items[a]
        elif command[0] == 'p':
            a, b = command[1:].split('/')
            index_a, index_b = items.index(values[a]), items.index(values[b])
            items[index_a], items[index_b] = items[index_b], items[index_a]
    return ''.join([values_reversed[i] for i in items])

@function_timer
def part1(data):
    return dance('abcdefghijklmnop', data)




@function_timer
def part2(data):
    value = dance('abcdefghijklmnop', data)

    loop = 1
    while value != 'abcdefghijklmnop':
        loop += 1
        value = dance(value, data)
    remaining = 1_000_000_000 % loop
    for i in range(remaining):
        value = dance(value, data)
    return value

def main():
    data = get_input(16, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
