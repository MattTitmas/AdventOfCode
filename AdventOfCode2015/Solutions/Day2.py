def part1():
    values = [
        [int(j) for j in i.split("x")]
        for i in open("input.txt", "r").read().split("\n")
    ]
    feet = 0
    for measurements in values:
        copy = measurements[:]
        minimum = min(copy)
        copy.remove(minimum)
        ndmin = min(copy)
        feet += minimum * ndmin
        l = measurements[0]
        w = measurements[1]
        h = measurements[2]
        feet += 2 * l * w + 2 * w * h + 2 * h * l
    return feet


def part2():
    values = [
        [int(j) for j in i.split("x")]
        for i in open("input.txt", "r").read().split("\n")
    ]
    feet = 0

    for measurements in values:
        copy = measurements[:]
        minimum = min(copy)
        copy.remove(minimum)
        ndmin = min(copy)
        feet += minimum * 2 + ndmin * 2
        feet += measurements[0] * measurements[1] * measurements[2]
    return feet


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
