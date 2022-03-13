File = open("Input.txt").read().split("\n")

BagDictionary = {}
    
for line in File:
    CurrentBag = line.split(" contain ")[0].split(" bags")[0]
    if ("no" in line.split(" contain ")[1]):
        ContainedBags = []
    else:
        ContainedBags = [[x[0],x[2:].split(" bag")[0]] for x in line.split(" contain ")[1].split(", ")]
    BagDictionary[CurrentBag] = ContainedBags


def Part1():
    Amount = 0

    ToCheck = ["shiny gold"]
    for CheckingBag in ToCheck:
        for key in BagDictionary:
            for value in BagDictionary[key]:
                if CheckingBag in value[1]:
                    if not (key in ToCheck):
                        ToCheck.append(key)
                        Amount += 1
    return Amount
                    
def CountBags(colour):
    return 1 + sum(int(number)*CountBags(colour) for number, colour in BagDictionary[colour])
    
def Part2():
    print(BagDictionary["light indigo"])
    return CountBags("shiny gold") - 1
    





print(Part1())
print(Part2())
