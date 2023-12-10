from itertools import permutations


def part1():
    values = [
        [int(j) if j.isnumeric() else j.split(" to ") for j in i.split(" = ")]
        for i in open("input.txt", "r").read().split("\n")
    ]
    routes = {}
    for i in values:
        if i[0][0] not in routes:
            routes[i[0][0]] = {i[0][1]: i[1]}
        else:
            routes[i[0][0]][i[0][1]] = i[1]

        if i[0][1] not in routes:
            routes[i[0][1]] = {i[0][0]: i[1]}
        else:
            routes[i[0][1]][i[0][0]] = i[1]
    val = float("inf")
    for i in permutations(list(routes.keys())):
        distance = 0
        for j in range(0, len(i) - 1):
            distance += routes[i[j]][i[j + 1]]
        val = min(val, distance)
    return val


def part2():
    values = [
        [int(j) if j.isnumeric() else j.split(" to ") for j in i.split(" = ")]
        for i in open("input.txt", "r").read().split("\n")
    ]
    routes = {}
    for i in values:
        if i[0][0] not in routes:
            routes[i[0][0]] = {i[0][1]: i[1]}
        else:
            routes[i[0][0]][i[0][1]] = i[1]

        if i[0][1] not in routes:
            routes[i[0][1]] = {i[0][0]: i[1]}
        else:
            routes[i[0][1]][i[0][0]] = i[1]
    val = -float("inf")
    for i in permutations(list(routes.keys())):
        distance = 0
        for j in range(0, len(i) - 1):
            distance += routes[i[j]][i[j + 1]]
        val = max(val, distance)
    return val


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
