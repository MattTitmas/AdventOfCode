def part1():
    file = open("input.txt", "r").read()
    pointer = 0
    weight = 0
    while pointer < len(file):
        if file[pointer] == "(":
            amount = ""
            duplicate = ""
            changingAmount = True
            pointer += 1
            while file[pointer] != ")":
                if file[pointer] == "x":
                    changingAmount = False
                elif changingAmount:
                    amount += file[pointer]
                else:
                    duplicate += file[pointer]
                pointer += 1
            weight += int(amount) * int(duplicate)
            pointer += int(amount)
        else:
            weight += 1
        pointer += 1
    return weight


def part2():
    file = open("input.txt", "r").read()
    weights = [1] * len(file)
    weight = 0
    pointer = 0
    while pointer < len(file):
        if file[pointer] == "(":
            amount = ""
            duplicate = ""
            changingAmount = True
            pointer += 1
            while file[pointer] != ")":
                if file[pointer] == "x":
                    changingAmount = False
                elif changingAmount:
                    amount += file[pointer]
                else:
                    duplicate += file[pointer]
                pointer += 1
            for j in range(1, int(amount) + 1):
                weights[pointer + j] *= int(duplicate)
        else:
            weight += weights[pointer]
        pointer += 1
    return weight


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")
