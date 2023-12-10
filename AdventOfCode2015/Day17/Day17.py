from itertools import combinations


def part1():
    values = [int(i) for i in open("input.txt", "r").read().split("\n")]
    total = 0
    for i in range(len(values)):
        for j in combinations(values, i):
            if sum(j) == 150:
                total += 1
    return total


def part2():
    values = [int(i) for i in open("input.txt", "r").read().split("\n")]
    total = 0
    min = -1
    for i in range(len(values)):
        for j in combinations(values, i):
            if sum(j) == 150:
                if min == -1:
                    min = i
                if i == min:
                    total += 1
                else:
                    return total


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
