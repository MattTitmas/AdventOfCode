def part1():
    values = [list(i) for i in open("input.txt", "r").read().split("\n")]
    colLen = len(values)
    rowLen = len(values[0])
    prev = [["" for j in row] for row in values]
    count = 0
    while True:
        count += 1
        copy = [row[:] for row in values]
        # East Facing
        for i in range(len(copy)):
            for j in range(len(copy[i])):
                if copy[i][(j + 1) % rowLen] == "." and copy[i][j] == ">":
                    values[i][j % rowLen] = "."
                    values[i][(j + 1) % rowLen] = ">"
        copy = [row[:] for row in values]
        # South Facing
        for i in range(len(copy)):
            for j in range(len(copy[i])):
                if copy[(i + 1) % colLen][j] == "." and copy[i][j] == "v":
                    values[i % colLen][j] = "."
                    values[(i + 1) % colLen][j] = "v"
        allMatching = True
        for i in range(len(values)):
            for j in range(len(values[i])):
                if prev[i][j] != values[i][j]:
                    allMatching = False
        if allMatching:
            return count
        prev = [row[:] for row in values]

    print(values)
    return 0


def part2():
    commands = open("input.txt", "r").read().split("\n")
    return 0


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
