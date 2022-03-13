from math import prod

def part1():
    file = [i.split(" ") for i in open("input.txt","r").read().split("\n\n")[0].split("\n")]
    registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    while i < len(file):
        command = file[i]
        if command[0] == "cpy":
            registers[command[2]] = int(command[1]) if command[1].lstrip("-").isnumeric() else registers[command[1]]
        elif command[0] == "inc":
            registers[command[1]] += 1
        elif command[0] == "dec":
            registers[command[1]] -= 1
        elif command[0] == "jnz":
            i += (int(command[2])-1 if command[2].lstrip("-").isnumeric() else registers[command[2]]-1) if (int(command[1]) if command[1].lstrip("-").isnumeric() else registers[command[1]]) != 0 else 0
        elif command[0] == "tgl":
            if i + int(registers[command[1]]) < len(file):
                commandToChange = file[i+int(registers[command[1]])]
                if len(commandToChange) == 2:
                    if commandToChange[0] == "inc":
                        commandToChange[0] = "dec"
                    else:
                        commandToChange[0] = "inc"
                elif len(commandToChange) == 3:
                    if commandToChange[0] == "jnz":
                        commandToChange[0] = "cpy"
                    else:
                        commandToChange[0] = "jnz"

        i += 1
    return registers['a']


def part2():
    file = [i.split(" ") for i in open("input.txt","r").read().split("\n\n")[1].split("\n")]
    registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    while i < len(file):
        command = file[i]
        if command[0] == "cpy":
            registers[command[2]] = int(command[1]) if command[1].lstrip("-").isnumeric() else registers[command[1]]
        elif command[0] == "inc":
            registers[command[1]] += 1
        elif command[0] == "dec":
            registers[command[1]] -= 1
        elif command[0] == "jnz":
            i += (int(command[2])-1 if command[2].lstrip("-").isnumeric() else registers[command[2]]-1) if (int(command[1]) if command[1].lstrip("-").isnumeric() else registers[command[1]]) != 0 else 0
        elif command[0] == "mul":
            registers[command[3]] = registers[command[1]] * registers[command[2]]
        elif command[0] == "tgl":
            if i + int(registers[command[1]]) < len(file):
                commandToChange = file[i+int(registers[command[1]])]
                if len(commandToChange) == 2:
                    if commandToChange[0] == "inc":
                        commandToChange[0] = "dec"
                    else:
                        commandToChange[0] = "inc"
                elif len(commandToChange) == 3:
                    if commandToChange[0] == "jnz":
                        commandToChange[0] = "cpy"
                    else:
                        commandToChange[0] = "jnz"

        i += 1
    return registers['a']
print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")