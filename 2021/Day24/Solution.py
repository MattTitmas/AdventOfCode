from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    commands = data.split("\n")

    def inputInstruction(modelNo, current):
        return modelNo[current], current + 1

    instructions = {
        "inp": inputInstruction,
        "add": lambda x, y: x + y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x // y,
        "mod": lambda x, y: x % y,
        "eql": lambda x, y: 1 if x == y else 0
    }

    def reduce(model):
        model[-1] -= 1
        for i in range(len(model) - 1, 1, -1):
            if model[i] < 1:
                model[i] = 9
                model[i - 1] -= 1
        return model

    modelNo = [9, 1, 6, 9, 9, 3, 9, 4, 8, 9, 5, 0, 0, 0]
    while True:
        currentNoInput = 0
        variables = {"w": 0, "x": 0, "y": 0, "z": 0}
        for command in commands:
            opcode = command.split(" ")[0]
            storeLoc = command.split(" ")[1]
            operands = [int(i) if i.lstrip("-").isnumeric() else variables[i] for i in command.split(" ")[1:]]
            instruction = instructions[opcode]

            if len(operands) == 1:
                val, currentNoInput = instruction(modelNo, currentNoInput)
                variables[storeLoc] = val
            else:
                variables[storeLoc] = instruction(operands[0], operands[1])

        if variables["z"] == 0:
            return "".join([str(i) for i in modelNo])
        modelNo = reduce(modelNo)


@function_timer_avg
def part2(data):
    commands = data.split("\n")

    def inputInstruction(modelNo, current):
        return modelNo[current], current + 1

    instructions = {
        "inp": inputInstruction,
        "add": lambda x, y: x + y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x // y,
        "mod": lambda x, y: x % y,
        "eql": lambda x, y: 1 if x == y else 0
    }

    def reduce(model):
        model[-1] += 1
        for i in range(len(model) - 1, 1, -1):
            if model[i] > 9:
                model[i] = 1
                model[i - 1] += 1
        return model

    modelNo = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    while True:
        currentNoInput = 0
        variables = {"w": 0, "x": 0, "y": 0, "z": 0}
        for command in commands:
            opcode = command.split(" ")[0]
            storeLoc = command.split(" ")[1]
            operands = [int(i) if i.lstrip("-").isnumeric() else variables[i] for i in command.split(" ")[1:]]
            instruction = instructions[opcode]

            if len(operands) == 1:
                val, currentNoInput = instruction(modelNo, currentNoInput)
                variables[storeLoc] = val
            else:
                variables[storeLoc] = instruction(operands[0], operands[1])
        if variables["z"] == 0:
            return "".join([str(i) for i in modelNo])
        modelNo = reduce(modelNo)


def main():
    data = get_input(24, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
