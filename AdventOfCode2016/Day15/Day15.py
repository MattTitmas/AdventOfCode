def part1():
    positions = {
        int(i.split("#")[1][0]): int(i.split("position ")[1][:-1])
        for i in open("input.txt").read().split("\n")[:-1]
    }
    possiblePositions = {
        int(i.split("#")[1][0]): int(i.replace("positions;", "has").split("has ")[1])
        for i in open("input.txt").read().split("\n")
    }
    time = 0
    while True:
        for key, value in positions.items():
            positions[key] = (value + 1) % possiblePositions[key]

        allZero = True
        for key in positions.keys():
            position = (positions[key] + key) % possiblePositions[key]
            if position != 0:
                allZero = False
                break
        if allZero:
            return time + 1
        time += 1


def part2():
    positions = {
        int(i.split("#")[1][0]): int(i.split("position ")[1][:-1])
        for i in open("input.txt").read().split("\n")
    }
    possiblePositions = {
        int(i.split("#")[1][0]): int(i.replace("positions;", "has").split("has ")[1])
        for i in open("input.txt").read().split("\n")
    }
    time = 0
    while True:
        for key, value in positions.items():
            positions[key] = (value + 1) % possiblePositions[key]

        allZero = True
        for key in positions.keys():
            position = (positions[key] + key) % possiblePositions[key]
            if position != 0:
                allZero = False
                break
        if allZero:
            return time + 1
        time += 1


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")
