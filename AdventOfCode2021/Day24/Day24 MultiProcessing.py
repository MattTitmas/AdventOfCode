from multiprocessing import Pool
from time import time

modelNo = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
commands = open("input.txt","r").read().split("\n")

def part1(model):
    if "0" in str(model):
        return False

    modelNo = [int(x) for x in str(model)]

    def inputInstruction(modelNo, current):
        return modelNo[current], current+1

    instructions = {
        "inp": inputInstruction,
        "add": lambda x, y: x + y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x // y,
        "mod": lambda x, y: x % y,
        "eql": lambda x, y: 1 if x == y else 0
    }
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
        return "".join([str(i) for i in modelNo]), True
    return False


if __name__ == '__main__':
    start = time()

    vals = range(99999999000000, 99999999999999)
    poolFour = Pool(processes=4)
    vals = poolFour.map(part1, vals)
    end = time()
    print(end-start)
    #print([i[0] for i in filter(lambda x: x[1] == True, vals)])

'''
    numbers = [i for i in range(5000000)]
    poolFour = Pool(processes=4)
    vals = poolFour.map(is_prime, numbers)
    end = time()
    print(end-start)
    #print([i[0] for i in filter(lambda x: x[1] == True, vals)])

    start = time()
    numbers = [i for i in range(5000000)]
    poolOne = Pool(processes=1)
    vals = poolOne.map(is_prime, numbers)
    end = time()
    print(end-start)
    #print([i[0] for i in filter(lambda x: x[1] == True, vals)])
'''