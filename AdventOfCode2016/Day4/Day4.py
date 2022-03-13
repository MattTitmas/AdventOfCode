from collections import Counter

def part1():
    values = [i[:-1].split("[") for i in open("input.txt").read().split("\n")]
    total = 0
    for i in values:
        count = Counter(i[0])
        id = i[0].split("-")[-1]
        del count["-"]
        for j in id:
            del count[j]
        str = "".join([i[0] for i in sorted(count.most_common(), key=lambda x: (-x[1], x[0]))])
        if str[:5] == i[1]:
            total += int(id)
    return total


def part2():
    values = [i[:-1].split("[") for i in open("input.txt").read().split("\n")]
    total = 0
    for i in values:
        ID = int(i[0].split("-")[-1])
        shift = int(i[0].split("-")[-1]) % 26
        toPrint = ""
        for j in i[0]:
            newChar = ord(j) + shift
            if newChar > ord('z'):
                newChar -= 26
            finalLetter = chr(newChar)
            if j == "-":
                toPrint += " "
            else:
                toPrint += finalLetter
        if "northpole" in toPrint:
            return ID



print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")