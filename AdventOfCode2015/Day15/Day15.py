def part1():
    values = {
        i.split(":")[0]: {
            j.split(" ")[0]: int(j.split(" ")[1]) for j in i.split(": ")[1].split(", ")
        }
        for i in open("input.txt", "r").read().split("\n")
    }
    maxScore = 0
    for sprinkles in range(0, 101):
        for peanut in range(0, 100 - sprinkles):
            for frosting in range(0, 100 - sprinkles - peanut):
                if sprinkles + peanut + frosting <= 100:
                    sugar = 100 - (sprinkles + peanut + frosting)
                    totalCapacity = max(
                        0,
                        values["Sprinkles"]["capacity"] * sprinkles
                        + values["PeanutButter"]["capacity"] * peanut
                        + values["Frosting"]["capacity"] * frosting
                        + values["Sugar"]["capacity"] * sugar,
                    )
                    totalDurability = max(
                        0,
                        values["Sprinkles"]["durability"] * sprinkles
                        + values["PeanutButter"]["durability"] * peanut
                        + values["Frosting"]["durability"] * frosting
                        + values["Sugar"]["durability"] * sugar,
                    )
                    totalFlavour = max(
                        0,
                        values["Sprinkles"]["flavor"] * sprinkles
                        + values["PeanutButter"]["flavor"] * peanut
                        + values["Frosting"]["flavor"] * frosting
                        + values["Sugar"]["flavor"] * sugar,
                    )
                    totalTexture = max(
                        0,
                        values["Sprinkles"]["texture"] * sprinkles
                        + values["PeanutButter"]["texture"] * peanut
                        + values["Frosting"]["texture"] * frosting
                        + values["Sugar"]["texture"] * sugar,
                    )
                    score = (
                        totalCapacity * totalDurability * totalFlavour * totalTexture
                    )
                    maxScore = max(maxScore, score)
    return maxScore


def part2():
    values = {
        i.split(":")[0]: {
            j.split(" ")[0]: int(j.split(" ")[1]) for j in i.split(": ")[1].split(", ")
        }
        for i in open("input.txt", "r").read().split("\n")
    }
    maxScore = 0
    for sprinkles in range(0, 101):
        for peanut in range(0, 101):
            for frosting in range(0, 101):
                if sprinkles + peanut + frosting <= 100:
                    sugar = 100 - (sprinkles + peanut + frosting)
                    totalCapacity = max(
                        0,
                        values["Sprinkles"]["capacity"] * sprinkles
                        + values["PeanutButter"]["capacity"] * peanut
                        + values["Frosting"]["capacity"] * frosting
                        + values["Sugar"]["capacity"] * sugar,
                    )
                    totalDurability = max(
                        0,
                        values["Sprinkles"]["durability"] * sprinkles
                        + values["PeanutButter"]["durability"] * peanut
                        + values["Frosting"]["durability"] * frosting
                        + values["Sugar"]["durability"] * sugar,
                    )
                    totalFlavour = max(
                        0,
                        values["Sprinkles"]["flavor"] * sprinkles
                        + values["PeanutButter"]["flavor"] * peanut
                        + values["Frosting"]["flavor"] * frosting
                        + values["Sugar"]["flavor"] * sugar,
                    )
                    totalTexture = max(
                        0,
                        values["Sprinkles"]["texture"] * sprinkles
                        + values["PeanutButter"]["texture"] * peanut
                        + values["Frosting"]["texture"] * frosting
                        + values["Sugar"]["texture"] * sugar,
                    )
                    totalCalories = (
                        values["Sprinkles"]["calories"] * sprinkles
                        + values["PeanutButter"]["calories"] * peanut
                        + values["Frosting"]["calories"] * frosting
                        + values["Sugar"]["calories"] * sugar
                    )
                    score = (
                        totalCapacity * totalDurability * totalFlavour * totalTexture
                    )
                    if totalCalories == 500:
                        maxScore = max(maxScore, score)
    return maxScore


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
