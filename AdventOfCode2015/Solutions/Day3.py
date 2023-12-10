def part1():
    values = list(open("input.txt", "r").read())
    houses = {}

    x = 0
    y = 0
    houses[(x, y)] = 1 if (x, y) not in houses else houses[x, y] + 1
    for k in values:
        if k == ">" or k == "<":
            x += 1 if k == ">" else -1
        else:
            y += 1 if k == "^" else -1
        houses[(x, y)] = 1 if (x, y) not in houses else houses[x, y] + 1
    return len(houses)


def part2():
    values = list(open("input.txt", "r").read())
    houses = {}

    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    houses[(0, 0)] = 2
    for c, k in enumerate(values):
        if k == ">" or k == "<":
            x1 += ((c + 1) % 2) * (1 if k == ">" else -1)
            x2 += (c % 2) * (1 if k == ">" else -1)
        else:
            y1 += ((c + 1) % 2) * (1 if k == "^" else -1)
            y2 += (c % 2) * (1 if k == "^" else -1)
        houses[(x1, y1)] = 1 if (x1, y1) not in houses else houses[x1, y1] + 1
        houses[(x2, y2)] = 1 if (x2, y2) not in houses else houses[x2, y2] + 1
    return len(houses)


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
