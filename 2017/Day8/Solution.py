from aoc import get_input
from utils import function_timer_avg, function_timer

instructions = {
    'inc': lambda x, y, _registers: _registers.get(x, 0) + int(y),
    'dec': lambda x, y, _registers: _registers.get(x, 0) - int(y),
}

comparisons = {
    '==': lambda x, y, _registers: _registers.get(x, 0) == int(y),
    '<': lambda x, y, _registers: _registers.get(x, 0) < int(y),
    '>': lambda x, y, _registers: _registers.get(x, 0) > int(y),
    '<=': lambda x, y, _registers: _registers.get(x, 0) <= int(y),
    '>=': lambda x, y, _registers: _registers.get(x, 0) >= int(y),
    '!=': lambda x, y, _registers: _registers.get(x, 0) != int(y),
}


@function_timer_avg
def part1(data):
    registers = dict()
    for statement in data.split('\n'):
        command, condition = statement.split(' if ')
        to_change, command, value = command.split(' ')
        reg_1, condition, reg_2 = condition.split(' ')
        if comparisons[condition](reg_1, reg_2, registers):
            registers[to_change] = instructions[command](to_change, value, registers)

    return max(registers.values())


@function_timer_avg
def part2(data):
    registers = dict()
    max_so_far = -1
    for statement in data.split('\n'):
        command, condition = statement.split(' if ')
        to_change, command, value = command.split(' ')
        reg_1, condition, reg_2 = condition.split(' ')
        if comparisons[condition](reg_1, reg_2, registers):
            new_val = instructions[command](to_change, value, registers)
            max_so_far = max(new_val, max_so_far)
            registers[to_change] = new_val

    return max_so_far


def main():
    data = get_input(8, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
