from itertools import permutations


def part1():
    nodes = {
        (int(i.split()[0].split("-")[1][1:]), int(i.split()[0].split("-")[2][1:])): [
            int(i.split()[1][:-1]),
            int(i.split()[2][:-1]),
            int(i.split()[3][:-1]),
            int(i.split()[4][:-1]),
        ]
        for i in open("input.txt").read().split("\n")[2:]
    }
    count = 0
    for key, value in nodes.items():
        for compKey, compValue in nodes.items():
            if key != compKey and value[1] != 0 and value[1] < compValue[2]:
                count += 1
    return count


def part2():
    nodes = {
        (int(i.split()[0].split("-")[1][1:]), int(i.split()[0].split("-")[2][1:])): [
            int(i.split()[1][:-1]),
            int(i.split()[2][:-1]),
            int(i.split()[3][:-1]),
            int(i.split()[4][:-1]),
        ]
        for i in open("input.txt").read().split("\n")[2:]
    }
    for y in range(0, 28):
        for x in range(0, 38):
            if nodes[(x, y)][1] == 0:
                print("-", end="")
            elif nodes[(x, y)][1] < 100:
                print(".", end="")
            else:
                print("#", end="")
        print()


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")
