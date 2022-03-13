import math

keyPad1 = {
    (0, 0): 1,
    (1, 0): 2,
    (2, 0): 3,
    (0, 1): 4,
    (1, 1): 5,
    (2, 1): 6,
    (0, 2): 7,
    (1, 2): 8,
    (2, 2): 9,
}


keyPad2 = {
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    (-1, 0): "6",
    (-2, 0): "5",
    (0, -1): "3",
    (-1, -1): "2",
    (1, -1): "4",
    (0, -2): "1",
    (-1, 1): "A",
    (0, 1): "B",
    (1, 1): "C",
    (0, 2): "D"
}
def part1():
    values = open("input.txt","r").read().split("\n")
    xPos = 1; yPos = 1
    toRet = ""
    for i in values:
        for j in i:
            if j == "L":
                xPos = max(xPos-1, 0)
            elif j == "R":
                xPos = min(2, xPos+1)
            elif j == "U":
                yPos = max(yPos-1, 0)
            else:
                yPos = min(2, yPos+1)
        toRet += str(keyPad1[(xPos, yPos)])
    return toRet


def part2():
    values = open("input.txt", "r").read().split("\n")
    xPos = -2; yPos = 0
    toRet = ""
    for i in values:
        for j in i:
            oldX, oldY = xPos, yPos
            if j == "L":
                xPos -= 1
            elif j == "R":
                xPos += 1
            elif j == "U":
                yPos -= 1
            else:
                yPos += 1
            if (xPos, yPos) not in keyPad2:
                xPos = oldX
                yPos = oldY
        toRet += str(keyPad2[(xPos, yPos)])
    return toRet


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")