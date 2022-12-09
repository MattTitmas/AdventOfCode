from math import sin, cos, radians

from aoc import get_input
from utils import function_timer_avg, function_timer


def get_val(val: str, pointers):
    return pointers.get(val, 0) if val.isalpha() else int(val)


@function_timer
def part1(data):
    registers = {'pointer': 0}
    commands = {
        'set': lambda x, y, _pointers: get_val(y, _pointers),
        'sub': lambda x, y, _pointers: get_val(x, _pointers) - get_val(y, _pointers),
        'mul': lambda x, y, _pointers: get_val(x, _pointers) * get_val(y, _pointers),
        'jnz': lambda x, y, _pointers: 1 if get_val(x, _pointers) == 0 else get_val(y, _pointers)
    }
    total = 0
    lines = data.split('\n')
    while registers['pointer'] < len(lines):
        command, register_a, register_b = lines[registers['pointer']].split(' ')
        if command == 'jnz':
            registers['pointer'] += commands[command](register_a, register_b, registers)
        else:
            registers[register_a] = commands[command](register_a, register_b, registers)
            registers['pointer'] += 1
        if command == 'mul':
            total += 1
    return total


@function_timer
def part2(data):
    h = 0
    b = 81
    b = b * 100
    b = b + 100000
    c = b + 17000

    while True:  # E
        f = 1
        d = 2
        e = 2

        while True:  # B
            if b % d == 0:
                f = 0
            d = d + 1
            if d != b:
                continue
            if f == 0:
                h = h + 1
            if b == c:
                return h
            b = b + 17
            break



def main():
    data = get_input(23, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
