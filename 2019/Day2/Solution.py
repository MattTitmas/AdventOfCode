from typing import List

from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    functions = {
        1: lambda param, _program: _program[param[0]] + _program[param[1]],
        2: lambda param, _program: _program[param[0]] * _program[param[1]],
    }
    program = list(map(int, data.split(',')))
    program[1] = 12
    program[2] = 2
    i = 0
    while program[i] != 99:
        opcode, *parameter, output_location = program[i:i+4]
        program[output_location] = functions[opcode](parameter, program)
        i += 4
    return program[0]


@function_timer_avg
def part2(data):
    functions = {
        1: lambda param, _program: _program[param[0]] + _program[param[1]],
        2: lambda param, _program: _program[param[0]] * _program[param[1]],
    }
    program_store = list(map(int, data.split(',')))

    for i in range(0, 100):
        for j in range(0, 100):
            program = program_store[:]
            program[1] = j
            program[2] = i
            instruction_pointer = 0
            while program[instruction_pointer] != 99:
                opcode, *parameter, output_location = program[instruction_pointer:instruction_pointer+4]
                program[output_location] = functions[opcode](parameter, program)
                instruction_pointer += 4
            if program[0] == 19690720:
                return 100 * j + i


def main():
    data = get_input(2  , 2019)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
