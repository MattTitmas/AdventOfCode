from aoc import get_input
from utils import function_timer_avg, function_timer
from ..IntCode import IntCode


@function_timer
def part1(data):
    computer = IntCode(data, given_inputs=[1])
    computer.run_program()
    return computer.outputs[-1]


@function_timer
def part2(data):
    computer = IntCode(data, given_inputs=[5])
    computer.run_program()
    return computer.outputs[-1]


def main():
    data = get_input(5, 2019)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
