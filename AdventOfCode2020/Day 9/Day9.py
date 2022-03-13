def part1():
    Preamble =  25
    File = [int(x) for x in open("input.txt").read().split("\n")]
    for x in range(Preamble+1, len(File)):
        TrueForX = False
        for y in range(x-(Preamble+1), x):
            for z in range(x-(Preamble+1), x):
                if y != z:
                    if (File[z] + File[y] == File[x]):
                        TrueForX = True
        if not(TrueForX):
            return File[x]
        

def part2():
    File = [int(x) for x in open("input.txt").read().split("\n")]
    Wanted = 466456641
    for x in range(0,len(File)):
        Start = x
        Current = 0
        while Current < Wanted:
            Current += File[Start]
            Start += 1
        if (Current == Wanted):
            return min(File[x:Start])+max(File[x:Start])


print(part1())
print(part2())
