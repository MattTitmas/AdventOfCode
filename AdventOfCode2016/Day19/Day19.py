import math

def part1():
    noOfElves = int(open("input.txt","r").read())
    return int(bin(noOfElves)[3:]+bin(noOfElves)[2:][0], 2)

def part2():
    noOfElves = int(open("input.txt","r").read())
    power = math.floor(math.log(noOfElves) / math.log(3))
    b = int(math.pow(3, power))
    if noOfElves == b:
        return noOfElves
    if noOfElves - b <= b:
        return noOfElves - b
    return 2 * noOfElves - 3 * b

print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")