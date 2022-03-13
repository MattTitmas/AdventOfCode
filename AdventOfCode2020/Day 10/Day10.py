def part1():
    Input = [int(x) for x in open("input.txt").read().split("\n")]

    Start = 0

    Jumps = {}

    while len(Input) != 0:
        Smallest = float("inf")
        for x in Input:
            Smallest = min(Smallest, x-Start)
        if Smallest not in Jumps:
            Jumps[Smallest] = 1
        else:
            Jumps[Smallest] += 1
        Input.remove(Start+Smallest)
        Start = Start+Smallest

    Jumps[3] += 1
    return Jumps[1] * Jumps[3]

def part2():
    pass


print(part1())
print(part2())
