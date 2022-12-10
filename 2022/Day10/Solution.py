from aoc import get_input
from utils import function_timer, function_timer_avg


@function_timer_avg
def part1(data):
    x = 1
    wanted_signals = [20, 60, 100, 140, 180, 220]
    current_line, line_number = 'noop', 0
    time_with_line = 0
    total = 0
    for i in range(max(wanted_signals) + 2):
        if i in wanted_signals:
            total += x * i
        if time_with_line == 0:
            if current_line == 'noop':
                pass
            else:
                x += int(current_line.split(' ')[-1])
            current_line = data.split('\n')[line_number]
            if current_line == 'noop':
                time_with_line = 1
            else:
                time_with_line = 2
            line_number += 1
        time_with_line -= 1
    return total


@function_timer_avg
def part2(data):
    x = 1
    current_line, line_number, i = 'noop', 0, 0
    time_with_line = 0
    crt, crt_line = '', ''
    while line_number < len(data.split('\n')):
        if i % 40 == 0:
            crt += crt_line + '\n'
            crt_line = ''
        if time_with_line == 0:
            if current_line == 'noop':
                pass
            else:
                x += int(current_line.split(' ')[-1])
            current_line = data.split('\n')[line_number]
            if current_line == 'noop':
                time_with_line = 1
            else:
                time_with_line = 2
            line_number += 1
        crt_line += '⬜' if (i % 40) in range(x-1, x+2) else '⬛'
        time_with_line -= 1
        i += 1
    return crt + crt_line


def main():
    data = get_input(10, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
