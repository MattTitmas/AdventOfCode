def part1():
    values = [i for i in open("input.txt", "r").read().split("\n")]
    corresponding = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total = 0
    for line in values:
        lookingFor = ""
        for char in line:
            if char in "([{<":
                lookingFor += corresponding[char]
            else:
                if char != lookingFor[-1]:
                    total += scores[char]
                    break
                else:
                    lookingFor = lookingFor[:-1]
    return total


def part2():
    values = {i: "" for i in open("input.txt", "r").read().split("\n")}
    corresponding = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    total = 0
    toRemove = []
    for line in values:
        lookingFor = ""
        for char in line:
            if char in "([{<":
                lookingFor += corresponding[char]
            else:
                if char != lookingFor[-1]:
                    toRemove += [line]
                    break
                else:
                    lookingFor = lookingFor[:-1]
        values[line] = lookingFor[::-1]
    for line in toRemove:
        values.pop(line)
    storedScores = []
    for key, value in values.items():
        score = 0
        for i in value:
            score *= 5
            score += scores[i]
        storedScores.append(score)
    storedScores.sort()
    return storedScores[len(storedScores) // 2]


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
