def part1():
    values = [int(i) for i in open("input.txt", "r").read().split(",")]
    maximum = max(values)
    finalCost = float("inf")
    for i in range(maximum):
        totalCost = 0
        for cost in values:
            totalCost += abs(cost - i)
        if totalCost < finalCost:
            finalCost = totalCost
        else:
            return finalCost


def part2():
    values = [int(i) for i in open("input.txt", "r").read().split(",")]
    maximum = max(values)
    finalCost = float("inf")
    for i in range(maximum):
        totalCost = 0
        for cost in values:
            distance = abs(cost - i)
            totalCost += (distance * (distance + 1)) / 2
        if totalCost < finalCost:
            finalCost = totalCost
        else:
            return int(finalCost)

    values = open("input.txt", "r").read().split("\n")


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
