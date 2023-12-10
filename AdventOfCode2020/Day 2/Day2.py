def Part1():
    File = open("Input.txt").read().split("\n")
    Valid = 0
    for line in File:
        Minimum = int(line.split(" ")[0].split("-")[0])
        Maximum = int(line.split(" ")[0].split("-")[1])
        WantedLetter = line.split(" ")[1][0]
        Code = line.split(" ")[2]
        Incrementer = 0
        for letter in Code:
            if letter == WantedLetter:
                Incrementer += 1
        if Incrementer >= Minimum and Incrementer <= Maximum:
            Valid += 1
    return Valid


def Part2():
    File = open("Input.txt").read().split("\n")
    Valid = 0
    for line in File:
        Pos1 = int(line.split(" ")[0].split("-")[0])
        Pos2 = int(line.split(" ")[0].split("-")[1])
        WantedLetter = line.split(" ")[1][0]
        Code = line.split(" ")[2]
        if (Code[Pos1 - 1] == WantedLetter) ^ (Code[Pos2 - 1] == WantedLetter):
            Valid += 1
    return Valid


print(Part1())
print(Part2())
