import math


def part1():
    values = open("input.txt", "r").read().split(", ")
    degrees = 0
    xPosition, yPosition = 0, 0
    for command in values:
        if command[0] == "R":
            degrees += 90
        else:
            degrees -= 90
        degrees %= 360
        xPosition += int(command[1:]) * round(math.sin(math.radians(degrees)))
        yPosition += int(command[1:]) * round(math.cos(math.radians(degrees)))
    return abs(xPosition) + abs(yPosition)


def part2():
    values = open("input.txt", "r").read().split(", ")
    degrees = 0
    xPosition, yPosition = 0, 0
    visitedPositions = set()
    for command in values:
        if command[0] == "R":
            degrees += 90
        else:
            degrees -= 90
        degrees %= 360
        oldX = xPosition
        oldY = yPosition
        xPosition += int(command[1:]) * round(math.sin(math.radians(degrees)))
        yPosition += int(command[1:]) * round(math.cos(math.radians(degrees)))

        if oldY == yPosition:
            for x in range(oldX, xPosition):
                if (x, oldY) in visitedPositions:
                    print(x, oldY)
                    return x + oldY
                visitedPositions.add((x, oldY))

        if oldX == xPosition:
            for y in range(oldY, yPosition):
                if (oldX, y) in visitedPositions:
                    print(oldX, y)
                    return oldX + y
                visitedPositions.add((oldX, y))


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")
