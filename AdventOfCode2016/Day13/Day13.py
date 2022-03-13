from math import prod

def part1():
    file = int(open("input.txt","r").read())
    wantedxPos, wantedyPos = 31, 39
    foundPositions = {}
    currentDistances = {(1, 1): 0}

    while (wantedxPos, wantedyPos) not in foundPositions:
        currentX, currentY = -1, -1
        lowestDistance = float("inf")
        for (key, value) in currentDistances.items():
            if value < lowestDistance:
                currentX, currentY = key
                lowestDistance = value
        currentDistances.pop((currentX, currentY))
        foundPositions[(currentX, currentY)] = lowestDistance
        neighbours = []
        for i in range(max(0,currentX-1), currentX+2):
            for j in range(max(0, currentY-1), currentY+2):
                if abs(currentX-i) != abs(currentY-j) and not sum(int(x) for x in bin(i*i + 3*i + 2*i*j + j + j*j + file)[2:]) % 2:
                    neighbours.append((i, j))
        for neighbour in neighbours:
            if neighbour not in foundPositions:
                currentDistances[neighbour] = lowestDistance + 1 if neighbour not in currentDistances else min(currentDistances[neighbour], lowestDistance+1)
    return foundPositions[(31,39)]


def part2():
    file = int(open("input.txt","r").read())
    foundPositions = {}
    currentDistances = {(1, 1): 0}

    def minDist():
        val = float("inf")
        for value in currentDistances.values():
            val = min(val, value)
        return val

    while minDist() < 51:
        currentX, currentY = -1, -1
        lowestDistance = float("inf")
        for (key, value) in currentDistances.items():
            if value < lowestDistance:
                currentX, currentY = key
                lowestDistance = value
        currentDistances.pop((currentX, currentY))
        foundPositions[(currentX, currentY)] = lowestDistance
        neighbours = []
        for i in range(max(0,currentX-1), currentX+2):
            for j in range(max(0, currentY-1), currentY+2):
                if abs(currentX-i) != abs(currentY-j) and not sum(int(x) for x in bin(i*i + 3*i + 2*i*j + j + j*j + file)[2:]) % 2:
                    neighbours.append((i, j))
        for neighbour in neighbours:
            if neighbour not in foundPositions:
                currentDistances[neighbour] = lowestDistance + 1 if neighbour not in currentDistances else min(currentDistances[neighbour], lowestDistance+1)
    return len(foundPositions)


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")