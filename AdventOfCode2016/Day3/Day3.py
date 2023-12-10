def part1():
    values = [
        [int(j) for j in i.split() if j.isnumeric()]
        for i in open("input.txt", "r").read().split("\n")
    ]
    toRet = 0
    for i in values:
        i.sort()
        if i[0] + i[1] > i[2]:
            toRet += 1
    return toRet


def part2():
    values = [
        [int(j) for j in i.split() if j.isnumeric()]
        for i in open("input.txt", "r").read().split("\n")
    ]
    toRet = 0
    for i in range(0, len(values) - 2, 3):
        sizes0 = []
        sizes1 = []
        sizes2 = []
        for j in range(0, 3):
            sizes0.append(values[i + j][0])
            sizes1.append(values[i + j][1])
            sizes2.append(values[i + j][2])
        sizes0.sort()
        sizes1.sort()
        sizes2.sort()
        if sizes0[0] + sizes0[1] > sizes0[2]:
            toRet += 1
        if sizes1[0] + sizes1[1] > sizes1[2]:
            toRet += 1
        if sizes2[0] + sizes2[1] > sizes2[2]:
            toRet += 1
    return toRet


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")
