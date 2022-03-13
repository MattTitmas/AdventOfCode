def Part1():
    File = [int(x) for x in open("Input.txt").read().split()]
    for x in range(0, len(File)):
        Wanted = 2020 - File[x]

        for y in range(x+1, len(File)):
            if File[y] == Wanted:
                return Wanted *  File[x]

def Part2():
    File = [int(x) for x in open("Input.txt").read().split()]
    for x in range(0, len(File)):
        for y in range(x+1, len(File)):
            Wanted = 2020 - (File[x] + File[y])
            for z in range(y+1, len(File)):
                if File[z] == Wanted:
                    return File[z] * File[x] * File[y]

print(Part1())
print(Part2())
