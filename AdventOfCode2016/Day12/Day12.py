from math import prod

def part1():
    file = [i.split(" ") for i in open("input.txt","r").read().split("\n")]
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    while i < len(file):
        command = file[i]
        if command[0] == "cpy":
            registers[command[2]] = int(command[1]) if command[1].isnumeric() else registers[command[1]]
        elif command[0] == "inc":
            registers[command[1]] += 1
        elif command[0] == "dec":
            registers[command[1]] -= 1
        elif command[0] == "jnz":
            i += (int(command[2])-1) if (int(command[1]) if command[1].isnumeric() else registers[command[1]]) != 0 else 0
        i += 1
    return registers['a']


def part2():
    file = [i.split(" ") for i in open("input.txt","r").read().split("\n")]
    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    i = 0
    while i < len(file):
        command = file[i]
        if command[0] == "cpy":
            registers[command[2]] = int(command[1]) if command[1].isnumeric() else registers[command[1]]
        elif command[0] == "inc":
            registers[command[1]] += 1
        elif command[0] == "dec":
            registers[command[1]] -= 1
        elif command[0] == "jnz":
            i += (int(command[2])-1) if (int(command[1]) if command[1].isnumeric() else registers[command[1]]) != 0 else 0
        i += 1
    return registers['a']
print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")