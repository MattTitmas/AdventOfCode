from functools import lru_cache

energyCost = {"A": 1, "B": 10, "C": 100, "D": 1000}
wantedHallways = {"A": 0, "B": 1, "C": 2, "D": 3}

sizeOfRooms = 2


@lru_cache(maxsize=None)
def makeMove(hallway, rooms, totalEnergy=0):
    hallway = list(hallway)
    rooms = [list(i) for i in rooms]

    print(hallway)
    print(rooms)
    print(totalEnergy)
    print("\n")

    if [
        ["A"] * sizeOfRooms,
        ["B"] * sizeOfRooms,
        ["C"] * sizeOfRooms,
        ["D"] * sizeOfRooms,
    ] == rooms:
        return totalEnergy

    minEnergy = float("inf")
    # Move from hallway to room (if possible)
    for i in range(0, len(hallway)):
        if hallway[i] != "." and hallway[i] != "u":
            val = hallway[i]
            wanted = wantedHallways[val]
            wantedInHallway = 2 + (2 * wanted) + 1
            posOrNeg = -1 if i > wantedInHallway else 1
            blocked = not all(
                hallway[j] == "." or hallway[j] == "u"
                for j in range(i + posOrNeg, wantedInHallway + posOrNeg, posOrNeg)
            )
            roomForAmph = all(val == x for x in rooms[wanted])
            if not blocked and roomForAmph:
                rooms[wanted].append(val)
                hallway[i] = "."
                energyForThisMove = (
                    abs(i - wantedInHallway)
                    + 1
                    + (sizeOfRooms - len(rooms[wanted]) + 1)
                ) * energyCost[val]
                totalEnergy += energyForThisMove
                roomTuple = tuple(tuple(i) for i in rooms)
                energyOfThisPath = makeMove(tuple(hallway), roomTuple, totalEnergy)
                minEnergy = min(minEnergy, energyOfThisPath)
                hallway[i] = val
                rooms[wanted].pop()
                totalEnergy -= energyForThisMove

    # Move from rooms to hallway
    for i in range(len(rooms)):
        if rooms[i]:
            val = rooms[i].pop()
            wanted = wantedHallways[val]
            roomForAmph = wanted == i and all(val == x for x in rooms[wanted])
            if roomForAmph:
                rooms[i].append(val)
            else:
                movesToReachHallway = sizeOfRooms - len(rooms[i])
                possibleMovesInHallway = []
                for j in range(2 + (2 * i) - 1, -1, -1):
                    if hallway[j] != "." and hallway[j] != "u":
                        break
                    if hallway[j] != "u":
                        possibleMovesInHallway.append(j)
                for j in range(2 + (2 * i) + 1, len(hallway)):
                    if hallway[j] != "." and hallway[j] != "u":
                        break
                    if hallway[j] != "u":
                        possibleMovesInHallway.append(j)

                for j in possibleMovesInHallway:
                    hallway[j] = val
                    energyForThisMove = (
                        movesToReachHallway + abs((2 + (2 * i) - j))
                    ) * energyCost[val]
                    totalEnergy += energyForThisMove
                    roomTuple = tuple(tuple(i) for i in rooms)
                    energyOfThisPath = makeMove(tuple(hallway), roomTuple, totalEnergy)
                    minEnergy = min(minEnergy, energyOfThisPath)
                    hallway[j] = "."
                    totalEnergy -= energyForThisMove
                rooms[i].append(val)
    return minEnergy


def part1():
    values = [
        i.replace("#", "").replace(" ", "")
        for i in open("input.txt", "r").read().split("\n")[2:4]
    ]
    rooms = [[], [], [], []]
    hallway = ["."] * 11
    for i in range(4):
        hallway[2 + (2 * i)] = "u"
        rooms[i].append(values[1][i])
        rooms[i].append(values[0][i])
    roomTuple = tuple(tuple(i) for i in rooms)
    return makeMove(tuple(hallway), roomTuple)


def part2():
    return 0


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
