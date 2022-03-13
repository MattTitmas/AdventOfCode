def Part1():
    File = open("Input.txt").read().split("\n")

    Order = [3,1]
    CurrentLocation = [0,0]

    Trees = 0

    while (CurrentLocation[1] < len(File)-1):
        CurrentLocation[1] += Order[1]
        CurrentLocation[0] += Order[0]
        if File[CurrentLocation[1]][CurrentLocation[0] % 31] == "#":
            Trees += 1

    return Trees

def Part2():
    File = open("Input.txt").read().split("\n")

    Orders = [[1,2],[3,1],[1,1],[5,1],[7,1]]

    Multiply = 1

    for Order in Orders:
        CurrentLocation = [0,0]
        Trees = 0

        while (CurrentLocation[1] < len(File)-1):
            CurrentLocation[1] += Order[1]
            CurrentLocation[0] += Order[0]
            if File[CurrentLocation[1]][CurrentLocation[0] % 31] == "#":
                Trees += 1
        Multiply *= Trees

    return Multiply


print(Part1())
print(Part2())
