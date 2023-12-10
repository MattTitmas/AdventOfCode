def part1():
    commands = open("input.txt", "r").read().split("\n")

    def inputInstruction(modelNo, current):
        return modelNo[current], current + 1

    instructions = {
        "inp": inputInstruction,
        "add": lambda x, y: x + y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x // y,
        "mod": lambda x, y: x % y,
        "eql": lambda x, y: 1 if x == y else 0,
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
            operands = [
                int(i) if i.lstrip("-").isnumeric() else variables[i]
                for i in command.split(" ")[1:]
            ]
            instruction = instructions[opcode]

            if len(operands) == 1:
                val, currentNoInput = instruction(modelNo, currentNoInput)
                variables[storeLoc] = val
            else:
                variables[storeLoc] = instruction(operands[0], operands[1])

        if variables["z"] == 0:
            return "".join([str(i) for i in modelNo])
        modelNo = reduce(modelNo)


def part2():
    commands = open("input.txt", "r").read().split("\n")

    def inputInstruction(modelNo, current):
        return modelNo[current], current + 1

    instructions = {
        "inp": inputInstruction,
        "add": lambda x, y: x + y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x // y,
        "mod": lambda x, y: x % y,
        "eql": lambda x, y: 1 if x == y else 0,
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
            operands = [
                int(i) if i.lstrip("-").isnumeric() else variables[i]
                for i in command.split(" ")[1:]
            ]
            instruction = instructions[opcode]

            if len(operands) == 1:
                val, currentNoInput = instruction(modelNo, currentNoInput)
                variables[storeLoc] = val
            else:
                variables[storeLoc] = instruction(operands[0], operands[1])

        if variables["z"] == 0:
            return "".join([str(i) for i in modelNo])
        modelNo = reduce(modelNo)


print(f"answer to part1: {part1()}")  # 91699394894995
print(f"answer to part2: {part2()}")  # 51147191161261
