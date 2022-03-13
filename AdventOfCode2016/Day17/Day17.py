from hashlib import md5

def part1(code):
    openDoors = ["b","c","d","e","f"]
    def getOpen(string):
        hash = md5(string.encode()).hexdigest()
        movesMade = string[sum(1 for c in string if c.islower()):]
        positionX, positionY = movesMade.count("R") - movesMade.count("L"), movesMade.count("D")-movesMade.count("U")
        toRet = []
        for i in range(0,4):
            toRet.append(hash[i] in openDoors)
        if positionX == 0:
            toRet[2] = False
        if positionX == 3:
            toRet[3] = False
        if positionY == 0:
            toRet[0] = False
        if positionY == 3:
            toRet[1] = False
        return toRet

    def vault(string):
        movesMade = string[sum(1 for c in string if c.islower()):]
        positionX, positionY = movesMade.count("R") - movesMade.count("L"), movesMade.count("D") - movesMade.count("U")
        return (positionX, positionY) == (3,3)

    queue = [code]

    while True:
        currentCode = queue.pop(0)
        if vault(currentCode):
            return currentCode
        moves = getOpen(currentCode)
        for i in range(0, 4):
            if i == 0 and moves[i]:
                queue.append(currentCode + "U")
            elif i == 1 and moves[i]:
                queue.append(currentCode + "D")
            elif i == 2 and moves[i]:
                queue.append(currentCode + "L")
            elif i == 3 and moves[i]:
                queue.append(currentCode + "R")


def part2(code):
    openDoors = ["b","c","d","e","f"]
    def getOpen(string):
        hash = md5(string.encode()).hexdigest()
        movesMade = string[sum(1 for c in string if c.islower()):]
        positionX, positionY = movesMade.count("R") - movesMade.count("L"), movesMade.count("D")-movesMade.count("U")
        toRet = []
        for i in range(0,4):
            toRet.append(hash[i] in openDoors)
        if positionX == 0:
            toRet[2] = False
        if positionX == 3:
            toRet[3] = False
        if positionY == 0:
            toRet[0] = False
        if positionY == 3:
            toRet[1] = False
        return toRet

    def vault(string):
        movesMade = string[sum(1 for c in string if c.islower()):]
        positionX, positionY = movesMade.count("R") - movesMade.count("L"), movesMade.count("D") - movesMade.count("U")
        return (positionX, positionY) == (3,3)

    if vault(code):
        return len(code)-sum(1 for c in code if c.islower())

    moves = getOpen(code)
    val = 0
    for i in range(0, 4):
        if i == 0 and moves[i]:
            val = max(val, part2(code + "U"))
        elif i == 1 and moves[i]:
            val = max(val, part2(code + "D"))
        elif i == 2 and moves[i]:
            val = max(val, part2(code + "L"))
        elif i == 3 and moves[i]:
            val = max(val, part2(code + "R"))
    return val

print(f"Answer to part 1: {part1('pgflpeqp')}")
print(f"Answer to part 2: {part2('pgflpeqp')}")