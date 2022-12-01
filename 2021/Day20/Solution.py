def part1():
    key = "".join(open("input.txt").read().split("\n\n")[0].split("\n"))
    value = [list(i) for i in open("input.txt").read().split("\n\n")[1].split("\n")]
    lightPixels = set()

    for j in range(0, len(value)):
        for i in range(0, len(value[j])):
            if value[i][j] == "#":
                lightPixels.add((i, j))
    for counter in range(2):
        copySet = set()

        maximumX, maximumY = -float("inf"), -float("inf")
        minimumX, minimumY = float("inf"), float("inf")
        for i in lightPixels:
            maximumX = max(maximumX, i[1])
            maximumY = max(maximumY, i[0])
            minimumX = min(minimumX, i[1])
            minimumY = min(minimumY, i[0])

        for i in range(minimumY, maximumY+1):
            str = ""
            for j in range(minimumX, maximumX+1):
                if (i, j) in lightPixels:
                    str += "1"
                else:
                    str += "0"
            print(str)
        print("=-=-=-=-=")
        print(key[15])

        for pixel in lightPixels:
            yPos = pixel[0]
            xPos = pixel[1]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    str = ""
                    for y in range((yPos + i) - 1, (yPos + i) + 2):
                        for x in range((xPos + j) - 1, (xPos + j) + 2):
                            str += "1" if (y, x) in lightPixels else "0"
                    val = int(str, 2)
                    if key[val] == "#":
                        copySet.add((yPos+i, xPos+j))
        print(counter)

        if counter % 1 == 0:
            # add a border of "#"s
            pass

        lightPixels = set(copySet)

    '''
    maximumX, maximumY = -float("inf"), -float("inf")
    minimumX, minimumY = float("inf"), float("inf")
    for i in lightPixels:
        maximumX = max(maximumX, i[1])
        maximumY = max(maximumY, i[0])
        minimumX = min(minimumX, i[1])
        minimumY = min(minimumY, i[0])

    for i in range(minimumY, maximumY+1):
        str = ""
        for j in range(minimumX, maximumX+1):
            if (i, j) in copySet:
                str += "#"
            else:
                str += " "
        print(str)
    '''
    return len(lightPixels)


def part2():
    pass


print(f"answer to part1: {part1()}")
# print(f"answer to part2: {part2()}")
