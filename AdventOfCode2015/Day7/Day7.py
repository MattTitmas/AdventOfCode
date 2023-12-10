def part1():
    values = [
        [j for j in i.split(" ") if j != "->"]
        for i in open("input.txt", "r").read().split("\n\n")[0].split("\n")
    ]
    wires = dict()
    for _ in range(339):
        for command in values:
            toChange = command[-1]
            if len(command) == 4:
                # OR, AND, or SHIFT
                val1 = (
                    int(command[0])
                    if command[0].isnumeric()
                    else (wires[command[0]] if command[0] in wires else 0)
                )
                val2 = (
                    int(command[2])
                    if command[2].isnumeric()
                    else (wires[command[2]] if command[2] in wires else 0)
                )
                if command[1] == "OR":
                    wires[toChange] = val1 | val2
                elif command[1] == "AND":
                    wires[toChange] = val1 & val2
                elif command[1] == "RSHIFT":
                    wires[toChange] = val1 >> val2
                else:
                    wires[toChange] = val1 << val2
            elif len(command) == 3:
                val = (
                    int(command[1])
                    if command[1].isnumeric()
                    else (wires[command[1]] if command[1] in wires else 0)
                )
                wires[toChange] = val ^ 65535
            else:
                val = (
                    int(command[0])
                    if command[0].isnumeric()
                    else (wires[command[0]] if command[0] in wires else 0)
                )
                wires[toChange] = val
    return wires["a"]


def part2():
    values = [
        [j for j in i.split(" ") if j != "->"]
        for i in open("input.txt", "r").read().split("\n\n")[1].split("\n")
    ]
    wires = dict()
    for _ in range(339):
        for command in values:
            toChange = command[-1]
            if len(command) == 4:
                # OR, AND, or SHIFT
                val1 = (
                    int(command[0])
                    if command[0].isnumeric()
                    else (wires[command[0]] if command[0] in wires else 0)
                )
                val2 = (
                    int(command[2])
                    if command[2].isnumeric()
                    else (wires[command[2]] if command[2] in wires else 0)
                )
                if command[1] == "OR":
                    wires[toChange] = val1 | val2
                elif command[1] == "AND":
                    wires[toChange] = val1 & val2
                elif command[1] == "RSHIFT":
                    wires[toChange] = val1 >> val2
                else:
                    wires[toChange] = val1 << val2
            elif len(command) == 3:
                val = (
                    int(command[1])
                    if command[1].isnumeric()
                    else (wires[command[1]] if command[1] in wires else 0)
                )
                wires[toChange] = val ^ 65535
            else:
                val = (
                    int(command[0])
                    if command[0].isnumeric()
                    else (wires[command[0]] if command[0] in wires else 0)
                )
                wires[toChange] = val
    return wires["a"]


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
