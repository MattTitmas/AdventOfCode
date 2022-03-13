from time import time

def part1():
    traps = [i == "." for i in list(open("input.txt","r").read())]
    total = 0
    for _ in range(40):
        total += sum(traps)
        newLine = []
        for i in range(0, len(traps)):
            x = traps[i - 1] if i - 1 in range(0, len(traps)) else True
            y = traps[i + 1] if i + 1 in range(0, len(traps)) else True
            newLine.append(x == y)
        traps = newLine
    return total

def part2():
    traps = [i == "." for i in list(open("input.txt","r").read())]
    total = 0
    for _ in range(400000):
        total += sum(traps)
        newLine = []
        for i in range(0, len(traps)):
            x = traps[i - 1] if i - 1 in range(0, len(traps)) else True
            y = traps[i + 1] if i + 1 in range(0, len(traps)) else True
            newLine.append(x == y)
        traps = newLine
    return total

start = time()
print(f"Answer to part 1: {part1()}")
end = time()
print(end-start)
start = time()
print(f"Answer to part 2: {part2()}")
end = time()
print(end-start)