def part1():
    value = open("input.txt", "r").read().split("\n")[0]
    for i in range(0, len(value)):
        newChar = (
            value[i] if ord(value[i]) not in [111, 105, 108] else chr(ord(value[i]) + 1)
        )
        if newChar != value[i]:
            value = value[:i] + newChar + len(value[i + 1 :]) * "a"
            break

    def incrementString(string):
        newString = string
        incrementNext = True
        for i in range(len(string) - 1, -1, -1):
            if incrementNext:
                incrementNext = False
                if string[i] == "z":
                    string = string[:i] + "a" + string[i + 1 :]
                    incrementNext = True
                else:
                    newChar = (
                        chr(ord(string[i]) + 1)
                        if ord(string[i]) + 1 not in [111, 105, 108]
                        else chr(ord(string[i]) + 2)
                    )
                    string = string[:i] + newChar + string[i + 1 :]
            else:
                break

        return string

    value = incrementString(value)
    while True:
        first = any(
            ord(value[i]) == ord(value[i + 1]) - 1
            and ord(value[i]) == ord(value[i + 2]) - 2
            for i in range(0, len(value) - 2)
        )
        thirdTest = list(
            (ord(value[i]) == ord(value[i + 1]) for i in range(0, len(value) - 1))
        )
        third = False
        if sum(thirdTest) > 1:
            chars = set()
            for i in range(0, len(thirdTest)):
                if thirdTest[i]:
                    chars.add(value[i])
            if len(chars) > 1:
                third = True
        if first and third:
            return value
        value = incrementString(value)


def part2():
    value = open("input.txt", "r").read().split("\n")[1]
    for i in range(0, len(value)):
        newChar = (
            value[i] if ord(value[i]) not in [111, 105, 108] else chr(ord(value[i]) + 1)
        )
        if newChar != value[i]:
            value = value[:i] + newChar + len(value[i + 1 :]) * "a"
            break

    def incrementString(string):
        newString = string
        incrementNext = True
        for i in range(len(string) - 1, -1, -1):
            if incrementNext:
                incrementNext = False
                if string[i] == "z":
                    string = string[:i] + "a" + string[i + 1 :]
                    incrementNext = True
                else:
                    newChar = (
                        chr(ord(string[i]) + 1)
                        if ord(string[i]) + 1 not in [111, 105, 108]
                        else chr(ord(string[i]) + 2)
                    )
                    string = string[:i] + newChar + string[i + 1 :]
            else:
                break

        return string

    value = incrementString(value)
    while True:
        first = any(
            ord(value[i]) == ord(value[i + 1]) - 1
            and ord(value[i]) == ord(value[i + 2]) - 2
            for i in range(0, len(value) - 2)
        )
        thirdTest = list(
            (ord(value[i]) == ord(value[i + 1]) for i in range(0, len(value) - 1))
        )
        third = False
        if sum(thirdTest) > 1:
            chars = set()
            for i in range(0, len(thirdTest)):
                if thirdTest[i]:
                    chars.add(value[i])
            if len(chars) > 1:
                third = True
        if first and third:
            return value
        value = incrementString(value)


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
