def part1():
    values = open("input.txt", "r").read().split("\n")
    runningTotalActual = 0
    runningTotalCode = 0
    for message in values:
        pointer = 1
        total = 0
        while pointer < len(message) - 1:
            if message[pointer] != "\\":
                total += 1
                pointer += 1
            else:
                if message[pointer + 1] == "\\" or message[pointer + 1] == '"':
                    total += 1
                    pointer += 2
                else:
                    total += 1
                    pointer += 4

        runningTotalActual += total
        runningTotalCode += len(message)
    return runningTotalCode - runningTotalActual


def part2():
    values = open("input.txt", "r").read().split("\n")
    runningTotalActual = 0
    runningTotalCode = 0
    for message in values:
        newLength = 2
        for char in message:
            if char == '"' or char == "\\":
                newLength += 2
            else:
                newLength += 1
        runningTotalCode += newLength
        runningTotalActual += len(message)
    return runningTotalCode - runningTotalActual


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
