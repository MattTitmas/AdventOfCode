from itertools import permutations

def part1(key="abcdefgh"):
    rotate = {
        "right" : lambda txt, lst : txt[-int(lst[2]):] + txt[:-int(lst[2])],
        "left" : lambda txt, lst : txt[int(lst[2]):] + txt[:int(lst[2])],
}
    operations = [i.split(" ") for i in open("input.txt","r").read().split("\n")]
    for operation in operations:
        if operation[0] == "rotate":
            if operation[1] == "based":
                val = key.index(operation[-1])+1+(1 if key.index(operation[-1]) >= 4 else 0)
                key = rotate["right"](key, ["a","a",val % len(key)])
            else:
                key = rotate[operation[1]](key, operation)
        elif operation[0] == "swap":
            if operation[1] == "position":
                stringList = list(key)
                stringList[int(operation[2])], stringList[int(operation[5])] = \
                    stringList[int(operation[5])], stringList[int(operation[2])]
                key = "".join(stringList)
            else:
                stringList = list(key)
                stringList[key.index(operation[2])], stringList[key.index(operation[5])] = \
                    stringList[key.index(operation[5])], stringList[key.index(operation[2])]
                key = "".join(stringList)
        elif operation[0] == "reverse":
            lb, rb = int(operation[2]), int(operation[4])+1
            key = key[:lb] + key[lb:rb][::-1] + key[rb:]
        elif operation[0] == "move":
            value = key[int(operation[2])]
            key = key[:int(operation[2])] + key[int(operation[2]) + 1:]
            key = key[:int(operation[5])] + value + key[int(operation[5]):]
    return key

def part2():
    passwords = [''.join(p) for p in permutations('abcdefgh')]
    for string in passwords:
        if part1(string) == "fbgdceah":
            return string

print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")