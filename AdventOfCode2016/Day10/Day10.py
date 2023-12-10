from math import prod


def part1():
    file = [i.split(" ") for i in open("input.txt", "r").read().split("\n")]
    botsHolding = dict()
    botInstructions = dict()
    outputs = dict()
    for command in file:
        if command[0] == "value":
            value = int(command[1])
            botNo = int(command[5])
            botsHolding[botNo] = (
                [value]
                if botNo not in botsHolding
                else sorted(botsHolding[botNo] + [value])
            )
        else:
            botNo = int(command[1])
            outputLow = True if command[5] == "output" else False
            low = int(command[6])
            outputHigh = True if command[10] == "output" else False
            high = int(command[11])
            botInstructions[botNo] = [(low, outputLow), (high, outputHigh)]
    while True:
        copy = dict(botsHolding)
        for key, val in copy.items():
            if len(val) == 2:
                if val[0] == 17 and val[1] == 61:
                    return key
                low = botInstructions[key][0]
                high = botInstructions[key][1]
                if not low[1]:
                    botsHolding[low[0]] = (
                        [val[0]]
                        if low[0] not in botsHolding
                        else sorted(botsHolding[low[0]] + [val[0]])
                    )
                else:
                    outputs[low[0]] = (
                        [val[0]]
                        if low[0] not in outputs
                        else sorted(outputs[low[0]] + [val[0]])
                    )
                if not high[1]:
                    botsHolding[high[0]] = (
                        [val[1]]
                        if high[0] not in botsHolding
                        else sorted(botsHolding[high[0]] + [val[1]])
                    )
                else:
                    outputs[high[0]] = (
                        [val[1]]
                        if high[0] not in outputs
                        else sorted(outputs[high[0]] + [val[1]])
                    )
                botsHolding[key] = []


def part2():
    file = [i.split(" ") for i in open("input.txt", "r").read().split("\n")]
    botsHolding = dict()
    botInstructions = dict()
    outputs = dict()
    for command in file:
        if command[0] == "value":
            value = int(command[1])
            botNo = int(command[5])
            botsHolding[botNo] = (
                [value]
                if botNo not in botsHolding
                else sorted(botsHolding[botNo] + [value])
            )
        else:
            botNo = int(command[1])
            outputLow = True if command[5] == "output" else False
            low = int(command[6])
            outputHigh = True if command[10] == "output" else False
            high = int(command[11])
            botInstructions[botNo] = [(low, outputLow), (high, outputHigh)]
    copyChanged = True
    while copyChanged:
        copyChanged = False
        copy = dict(botsHolding)
        for key, val in copy.items():
            if len(val) == 2:
                low = botInstructions[key][0]
                high = botInstructions[key][1]
                if not low[1]:
                    botsHolding[low[0]] = (
                        [val[0]]
                        if low[0] not in botsHolding
                        else sorted(botsHolding[low[0]] + [val[0]])
                    )
                else:
                    outputs[low[0]] = (
                        [val[0]]
                        if low[0] not in outputs
                        else sorted(outputs[low[0]] + [val[0]])
                    )
                if not high[1]:
                    botsHolding[high[0]] = (
                        [val[1]]
                        if high[0] not in botsHolding
                        else sorted(botsHolding[high[0]] + [val[1]])
                    )
                else:
                    outputs[high[0]] = (
                        [val[1]]
                        if high[0] not in outputs
                        else sorted(outputs[high[0]] + [val[1]])
                    )
                botsHolding[key] = []
                copyChanged = True
    return prod(outputs[0]) * prod(outputs[1]) * prod(outputs[2])


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")
