def part1():
    value = open("input.txt", "r").read()
    for _ in range(40):
        currentChar = value[0]
        run = 1
        new = ""
        for i in range(1, len(value)):
            char = value[i]
            if char == currentChar:
                run += 1
            else:
                new += str(run) + currentChar
                currentChar = char
                run = 1
        new += str(run) + currentChar
        value = new
    return len(value)


def part2():
    value = open("input.txt", "r").read()
    for _ in range(50):
        currentChar = value[0]
        run = 1
        new = ""
        for i in range(1, len(value)):
            char = value[i]
            if char == currentChar:
                run += 1
            else:
                new += str(run) + currentChar
                currentChar = char
                run = 1
        new += str(run) + currentChar
        value = new
    return len(value)


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
