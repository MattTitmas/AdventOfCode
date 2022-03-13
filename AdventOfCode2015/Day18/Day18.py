def part1():
    values = [[True if j == "#" else False for j in i] for i in open("input.txt","r").read().split("\n")]
    for _ in range(100):
        copy = [row[:] for row in values]
        for i in range(0, len(values)):
            for j in range(0, len(values)):
                sum = 0
                for x in range(max(0,i - 1), min(len(values), i + 2)):
                    for y in range(max(0, j - 1), min(len(values), j + 2)):
                        if x != i or y != j:
                            sum += copy[x][y]
                if copy[i][j] and sum != 2 and sum != 3:
                    values[i][j] = False
                if not copy[i][j] and sum == 3:
                    values[i][j] = True
    total = 0
    for i in range(0, len(values)):
        for j in range(0, len(values)):
            total += 1 if values[i][j] else 0
    return total

def part2():
    values = [[True if j == "#" else False for j in i] for i in open("input.txt","r").read().split("\n")]
    for i, j in [(0,0),(0,99),(99,0),(99,99)]:
        values[i][j] = True
    for _ in range(100):
        copy = [row[:] for row in values]
        for i in range(0, len(values)):
            for j in range(0, len(values)):
                sum = 0
                for x in range(max(0,i - 1), min(len(values), i + 2)):
                    for y in range(max(0, j - 1), min(len(values), j + 2)):
                        if x != i or y != j:
                            sum += copy[x][y]
                if copy[i][j] and sum != 2 and sum != 3:
                    values[i][j] = False
                if not copy[i][j] and sum == 3:
                    values[i][j] = True
                if (i == 0 and j == 0) or (i == 99 and j == 99) or (i == 0 and j == 99) or (i == 99 and j == 0):
                    values[i][j] = True
    total = 0
    for i in range(0, len(values)):
        for j in range(0, len(values)):
            total += 1 if values[i][j] else 0
    return total

print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")

