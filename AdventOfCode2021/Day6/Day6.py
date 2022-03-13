def part1():
    values = [int(i) for i in open("input.txt","r").read().split(",")]
    amount = dict((x,values.count(x)) if x in values else (x,0 )for x in range(0,9))
    for i in range(80):
        numberZero = amount[0]
        for j in range(0,8):
            amount[j] = amount[j+1]
        amount[6] += numberZero
        amount[8] = numberZero
    return sum(amount.values())

def part2():
    values = [int(i) for i in open("input.txt","r").read().split(",")]
    amount = dict((x,values.count(x)) if x in values else (x,0 )for x in range(0,9))
    for i in range(256):
        numberZero = amount[0]
        for j in range(0,8):
            amount[j] = amount[j+1]
        amount[6] += numberZero
        amount[8] = numberZero
    return sum(amount.values())

print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
