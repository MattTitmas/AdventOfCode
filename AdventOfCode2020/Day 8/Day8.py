def part1():
    File = open("input.txt").read().split("\n")

    Acc = 0

    CurrentLine = 0

    Dictionary = {}

    while True:
        if str(CurrentLine) in Dictionary:
            break
        else:
            Dictionary[str(CurrentLine)] = 1

        if File[CurrentLine][0] == "n":
            CurrentLine += 1
        elif File[CurrentLine][0] == "a":
            Acc += int(File[CurrentLine].split(" ")[1])
            CurrentLine += 1
        else:
            CurrentLine += int(File[CurrentLine].split(" ")[1])
    return Acc


def part2():
    NotTerminates = True
    Length = len(open("input.txt").read().split("\n"))

    for x in range(Length):
        File = open("input.txt").read().split("\n")
        if File[x][0] == "n":
            File[x] = "jmp " + File[x].split(" ")[1]
        elif File[x][0] == "j":
            File[x] = "nop " + File[x].split(" ")[1]
        else:
            continue

        Acc = 0

        CurrentLine = 0

        Dictionary = {}

        while CurrentLine < Length:
            if str(CurrentLine) in Dictionary:
                break
            else:
                Dictionary[str(CurrentLine)] = 1
            if File[CurrentLine][0] == "n":
                CurrentLine += 1
            elif File[CurrentLine][0] == "a":
                Acc += int(File[CurrentLine].split(" ")[1])
                CurrentLine += 1
            else:
                CurrentLine += int(File[CurrentLine].split(" ")[1])
        if CurrentLine >= Length:
            return Acc


print(part1())
print(part2())
