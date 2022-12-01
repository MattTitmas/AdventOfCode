def part1():
    values = [[int(i) if i.isnumeric() else i for i in i.split(" ")] for i in open("input.txt","r").read().split("\n")]

    depth = 0
    horizontal = 0
    for i in values:
        if i[0] == "up":
            depth -= i[1]
        elif i[0] == "down":
            depth += i[1]
        elif i[0] == "forward":
            horizontal += i[1]

    return depth*horizontal

def part2():
    values = [[int(i) if i.isnumeric() else i for i in i.split(" ")] for i in open("input.txt","r").read().split("\n")]

    aim = 0
    depth = 0
    horizontal = 0
    for i in values:
        if i[0] == "up":
            aim -= i[1]
        elif i[0] == "down":
            aim += i[1]
        elif i[0] == "forward":
            horizontal += i[1]
            depth += aim * i[1]

    return depth*horizontal


    return total


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")

