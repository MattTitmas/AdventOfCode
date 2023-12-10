def part1():
    values = [int(i) for i in open("input.txt", "r").read().split("\n")]
    return sum([1 if values[i] > values[i - 1] else 0 for i in range(len(values))])


def part2():
    values = [int(i) for i in open("input.txt", "r").read().split("\n")]
    return sum(
        [
            1 if values[i + 1] + values[i + 2] > values[i - 1] + values[i + 1] else 0
            for i in range(1, len(values) - 2)
        ]
    )


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
