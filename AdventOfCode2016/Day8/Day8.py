def part1():
    values = [i.split(" ") for i in open("input.txt").read().split("\n")]
    lights = [
        [False] * 50,
        [False] * 50,
        [False] * 50,
        [False] * 50,
        [False] * 50,
        [False] * 50,
    ]

    for command in values:
        if command[0] == "rect":
            length, height = (int(i) for i in command[1].split("x"))
            for i in range(length):
                for j in range(height):
                    lights[j][i] = True
            pass

        elif command[1] == "column":
            column, rotation = int(command[2].split("=")[1]), int(command[-1])
            for _ in range(rotation):
                stored = lights[-1][column]
                for i in range(5, 0, -1):
                    lights[i][column] = lights[i - 1][column]
                lights[0][column] = stored
        else:
            row, rotation = int(command[2].split("=")[1]), int(command[-1])
            for _ in range(rotation):
                stored = lights[row][-1]
                for i in range(49, 0, -1):
                    lights[row][i] = lights[row][i - 1]
                lights[row][0] = stored
    total = 0
    for i in lights:
        for j in i:
            total += j
    return total


def part2():
    values = [i.split(" ") for i in open("input.txt").read().split("\n")]
    lights = [
        [False] * 50,
        [False] * 50,
        [False] * 50,
        [False] * 50,
        [False] * 50,
        [False] * 50,
    ]

    for command in values:
        if command[0] == "rect":
            length, height = (int(i) for i in command[1].split("x"))
            for i in range(length):
                for j in range(height):
                    lights[j][i] = True
            pass

        elif command[1] == "column":
            column, rotation = int(command[2].split("=")[1]), int(command[-1])
            for _ in range(rotation):
                stored = lights[-1][column]
                for i in range(5, 0, -1):
                    lights[i][column] = lights[i - 1][column]
                lights[0][column] = stored
        else:
            row, rotation = int(command[2].split("=")[1]), int(command[-1])
            for _ in range(rotation):
                stored = lights[row][-1]
                for i in range(49, 0, -1):
                    lights[row][i] = lights[row][i - 1]
                lights[row][0] = stored
    total = 0
    for i in lights:
        toPrint = ""
        count = 0
        for j in i:
            toPrint += "#" if j else " "
            count = (count + 1) % 5
            if count == 0:
                toPrint += " "
        print(toPrint)
    return total


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")
