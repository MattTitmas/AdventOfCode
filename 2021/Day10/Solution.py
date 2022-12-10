from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    values = [i for i in data.split("\n")]
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


@function_timer_avg
def part2(data):
    values = {i: "" for i in data.split("\n")}
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


def main():
    data = get_input(10, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
