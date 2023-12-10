def part1():
    values = [
        [int(j) for j in list(i)] for i in open("input.txt", "r").read().split("\n")
    ]
    total = 0
    for x in range(len(values)):
        for y in range(len(values[x])):
            minimumPoint = True
            for i in range(max(0, x - 1), min(x + 2, 100)):
                for j in range(max(0, y - 1), min(y + 2, 100)):
                    if abs(x - i) != abs(y - j):
                        minimumPoint = minimumPoint and (values[i][j] > values[x][y])

            if minimumPoint:
                total += 1 + (values[x][y])
    return total


def floodFill(values, x, y):
    if x < 0 or y < 0 or x > 99 or y > 99:
        return 0
    if values[x][y] == -1 or values[x][y] == 9:
        return 0
    total = 1
    values[x][y] = -1
    total += floodFill(values, x - 1, y)
    total += floodFill(values, x + 1, y)
    total += floodFill(values, x, y - 1)
    total += floodFill(values, x, y + 1)

    return total


def part2():
    values = [
        [int(j) for j in list(i)] for i in open("input.txt", "r").read().split("\n")
    ]
    maxThree = []
    for x in range(len(values)):
        for y in range(len(values[x])):
            minimumPoint = True
            for i in range(max(0, x - 1), min(x + 2, 100)):
                for j in range(max(0, y - 1), min(y + 2, 100)):
                    if abs(x - i) != abs(y - j):
                        minimumPoint = minimumPoint and (values[i][j] > values[x][y])
            if minimumPoint:
                value = floodFill(values, x, y)
                if len(maxThree) != 3:
                    maxThree.append(value)
                else:
                    if value > min(maxThree):
                        maxThree[maxThree.index(min(maxThree))] = value
    return maxThree[0] * maxThree[1] * maxThree[2]


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
