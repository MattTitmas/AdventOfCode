from collections import Counter

def part1():
    values = open("input.txt").read().split("\n")
    code = ""
    counters = [Counter(), Counter(), Counter(), Counter(), Counter(), Counter(), Counter(), Counter()]
    for word in values:
        for count, char in enumerate(word):
            counters[count][char] += 1
    for counter in counters:
        code += counter.most_common(1)[0][0]
    return code


def part2():
    values = open("input.txt").read().split("\n")
    code = ""
    counters = [Counter(), Counter(), Counter(), Counter(), Counter(), Counter(), Counter(), Counter()]
    for word in values:
        for count, char in enumerate(word):
            counters[count][char] += 1
    for counter in counters:
        code += counter.most_common()[:-2:-1][0][0]
    return code


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")