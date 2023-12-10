import hashlib


def part1():
    key = open("input.txt", "r").read()
    count = 0
    while True:
        count += 1
        newKey = key + str(count)

        if hashlib.md5(newKey.encode()).hexdigest()[:5] == "00000":
            return count


def part2():
    key = open("input.txt", "r").read()
    count = 0
    while True:
        count += 1
        newKey = key + str(count)
        if hashlib.md5(newKey.encode()).hexdigest()[:6] == "000000":
            return count


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
