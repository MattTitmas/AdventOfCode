def part1():
    record = [
        (int(i.split("-")[0]), int(i.split("-")[1]))
        for i in open("input.txt", "r").read().split("\n")
    ]
    record.sort()
    lowest = 0
    currentBoundary = 0
    while True:
        for low, high in record:
            if lowest in range(low, high):
                lowest = high + 1
                break
        else:
            return lowest


def part2():
    record = [
        (int(i.split("-")[0]), int(i.split("-")[1]))
        for i in open("input.txt", "r").read().split("\n")
    ]
    record.sort()
    i = 0
    s = 0
    for b in sorted(record):
        if i < b[0]:
            s += b[0] - i
        i = max(i, b[1] + 1)
    s += 2**32 - i
    return s


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")
