def part1():
    values = [[j for j in i.split(" ")] for i in open("input.txt").read().split("\n")]
    for i in range(len(values)):
        if len(values[i]) > 4:
            values[i] = values[i][1:]
        values[i].remove("through")
        values[i][1] = [int(i) for i in values[i][1].split(",")]
        values[i][2] = [int(i) for i in values[i][2].split(",")]
    lights = {}

    for action in values:
        for x in range(action[1][0], action[2][0] + 1):
            for y in range(action[1][1], action[2][1] + 1):
                if (x, y) in lights:
                    current = lights[(x, y)]
                else:
                    current = False
                if action[0] == "toggle":
                    current = not current
                elif action[0] == "on":
                    current = True
                else:
                    current = False
                lights[(x, y)] = current
    return sum(lights.values())


def part2():
    values = [[j for j in i.split(" ")] for i in open("input.txt").read().split("\n")]
    for i in range(len(values)):
        if len(values[i]) > 4:
            values[i] = values[i][1:]
        values[i].remove("through")
        values[i][1] = [int(i) for i in values[i][1].split(",")]
        values[i][2] = [int(i) for i in values[i][2].split(",")]
    lights = {}

    for action in values:
        for x in range(action[1][0], action[2][0] + 1):
            for y in range(action[1][1], action[2][1] + 1):
                if (x, y) in lights:
                    current = lights[(x, y)]
                else:
                    current = 0
                if action[0] == "toggle":
                    current += 2
                elif action[0] == "on":
                    current += 1
                else:
                    current = max(current - 1, 0)
                lights[(x, y)] = current
    return sum(lights.values())


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
