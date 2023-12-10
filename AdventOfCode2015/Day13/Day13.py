from itertools import permutations


def part1():
    value = [
        [
            i.split(" ")[0],
            i.split(" ")[-1][:-1],
            -int(i.split(" ")[3])
            if i.split(" ")[2] == "lose"
            else int(i.split(" ")[3]),
        ]
        for i in open("input.txt", "r").read().split("\n")
    ]
    happiness = dict()
    for relation in value:
        if relation[0] != "Myself" and relation[2] != "Myself":
            if relation[0] not in happiness:
                happiness[relation[0]] = {relation[1]: relation[2]}
            else:
                happiness[relation[0]][relation[1]] = relation[2]
    maxHappy = -float("inf")
    noOfPeople = 8
    for i in permutations(happiness.keys()):
        happy = 0
        for j in range(0, noOfPeople):
            happy += happiness[i[j]][i[(j + 1) % noOfPeople]]
            happy += happiness[i[(j + 1) % noOfPeople]][i[j]]
        maxHappy = max(happy, maxHappy)
    return maxHappy


def part2():
    value = [
        [
            i.split(" ")[0],
            i.split(" ")[-1][:-1],
            -int(i.split(" ")[3])
            if i.split(" ")[2] == "lose"
            else int(i.split(" ")[3]),
        ]
        for i in open("input.txt", "r").read().split("\n")
    ]
    happiness = dict()
    for relation in value:
        if relation[0] not in happiness:
            happiness[relation[0]] = {relation[1]: relation[2]}
        else:
            happiness[relation[0]][relation[1]] = relation[2]
    maxHappy = -float("inf")
    noOfPeople = 9
    for i in permutations(happiness.keys()):
        happy = 0
        for j in range(0, noOfPeople):
            happy += happiness[i[j]][i[(j + 1) % noOfPeople]]
            happy += happiness[i[(j + 1) % noOfPeople]][i[j]]
        maxHappy = max(happy, maxHappy)
    return maxHappy


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
