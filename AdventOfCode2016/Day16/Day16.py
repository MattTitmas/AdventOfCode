def part1():
    code = open("input.txt", "r").read()
    wantedLength = 272
    while len(code) < wantedLength:
        a = code
        b = code[::-1]
        code = a + "0" + "".join(["1" if i == "0" else "0" for i in list(b)])
    code = code[:wantedLength]
    chunkSize = 16
    checkSum = ""
    for i in range(0, len(code), chunkSize):
        checkSum += (
            "1" if sum(int(i) for i in list(code[i : i + chunkSize])) % 2 == 0 else "0"
        )
    return checkSum


def part2():
    code = open("input.txt", "r").read()
    wantedLength = 35651584
    while len(code) < wantedLength:
        a = code
        b = code[::-1]
        code = a + "0" + "".join(["1" if i == "0" else "0" for i in list(b)])
    code = code[:wantedLength]
    chunkSize = 2097152
    checkSum = ""
    for i in range(0, len(code), chunkSize):
        checkSum += (
            "1" if sum(int(i) for i in list(code[i : i + chunkSize])) % 2 == 0 else "0"
        )
    return checkSum


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")
