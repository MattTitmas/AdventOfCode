def Part1():
    File = [x.replace("\n", "") for x in open("Input.txt").read().split("\n\n")]
    Questions = 0
    for line in File:
        Questions += len("".join(set(line)))
    return Questions


def Part2():
    File = [x.split("\n") for x in open("Input.txt").read().split("\n\n")]
    Questions = 0
    for line in File:
        Common = line[0]
        for x in range(1, len(line)):
            Common = "".join(set(Common).intersection(line[x]))
        Questions += len(Common)
    return Questions


print(Part1())
print(Part2())
