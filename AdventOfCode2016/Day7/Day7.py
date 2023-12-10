from collections import Counter


def containsABBA(string: str) -> bool:
    for count in range(0, len(string) - 3):
        current = string[count]
        next = string[count + 1]
        if (
            current != next
            and string[count + 2] == next
            and string[count + 3] == current
        ):
            return True
    return False


def containsABA(strings: list) -> bool:
    for string in strings:
        if string[0] != "_":
            for count in range(0, len(string) - 2):
                if string[count] == string[count + 2]:
                    outside = string[count]
                    inside = string[count + 1]
                    for string2 in strings:
                        if string2[0] == "_":
                            for count2 in range(1, len(string2) - 2):
                                if (
                                    string2[count2] == inside
                                    and string2[count2 + 1] == outside
                                    and string2[count2 + 2] == inside
                                ):
                                    return True
    return False


def part1():
    values = [
        i.replace("[", "]_").split("]") for i in open("input.txt").read().split("\n")
    ]
    total = 0

    for i in values:
        toAdd = True
        abbaContained = False
        for j in i:
            if j[0] == "_" and containsABBA(j[1:]):
                toAdd = False
            elif j[0] != "_" and containsABBA(j):
                abbaContained = True
        total += abbaContained and toAdd
    return total


def part2():
    values = [
        i.replace("[", "]_").split("]") for i in open("input.txt").read().split("\n")
    ]
    total = 0
    for strings in values:
        total += containsABA(strings)
    return total


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")
