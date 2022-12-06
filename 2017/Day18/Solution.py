from collections import deque

from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    registers = dict()

    def get_val(y):
        if y.lstrip("-").isnumeric():
            return int(y)
        return registers[y]

    commands = {
        'set': lambda x, y, _registers: get_val(y),
        'add': lambda x, y, _registers: _registers.get(x, 0) + get_val(y),
        'mul': lambda x, y, _registers: _registers.get(x, 0) * get_val(y),
        'mod': lambda x, y, _registers: _registers.get(x, 0) % get_val(y),
    }
    previous_sound = -1
    command_data = data.split('\n')
    i = 0
    while True:
        change_i = True
        command, *arguments = command_data[i].split(' ')
        if command in commands:
            registers[arguments[0]] = commands[command](*arguments, registers)
        else:
            # snd, rcv, jgz
            if command == 'snd':
                previous_sound = registers[arguments[0]]
            elif (command == 'rcv') and (get_val(arguments[0]) != 0):
                return previous_sound
            elif command == 'jgz' and (get_val(arguments[0]) > 0):
                i += get_val(arguments[1])
                change_i = False
        if change_i:
            i += 1


@function_timer_avg
def part2(data):
    registers = [{'p': 0}, {'p': 1}]
    current_program = 0
    i = [0, 0]

    def get_val(y, program):
        if y.lstrip("-").isnumeric():
            return int(y)
        return registers[program].get(y, 0)

    commands = {
        'set': lambda x, y, _registers: get_val(y, current_program),
        'add': lambda x, y, _registers: _registers.get(x, 0) + get_val(y, current_program),
        'mul': lambda x, y, _registers: _registers.get(x, 0) * get_val(y, current_program),
        'mod': lambda x, y, _registers: _registers.get(x, 0) % get_val(y, current_program),
    }
    command_data = data.split('\n')
    total = 0
    waiting = [False, False]
    queues = [[], []]
    while True:
        if not waiting[0]:
            current_program = 0
        elif not waiting[1]:
            current_program = 1
        else:
            return total
        change_i = True
        command, *arguments = command_data[i[current_program]].split(' ')
        if command in commands:
            registers[current_program][arguments[0]] = commands[command](*arguments, registers[current_program])
        else:
            # snd, rcv, jgz
            if command == 'snd':
                queues[(current_program + 1) % 2] += [get_val(arguments[0], current_program)]
                waiting[(current_program + 1) % 2] = False
                if current_program == 1:
                    total += 1
                # sending sound
            elif command == 'rcv':
                if len(queues[current_program]) != 0:
                    registers[current_program][arguments[0]] = queues[current_program].pop(0)
                else:
                    waiting[current_program] = True
                    change_i = False
                # recieving sound
            elif command == 'jgz' and (get_val(arguments[0], current_program) > 0):
                i[current_program] += get_val(arguments[1], current_program)
                change_i = False
        if change_i:
            i[current_program] += 1


def main():
    data = get_input(18, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
